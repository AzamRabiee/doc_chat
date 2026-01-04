from typing import List, Literal, Dict

from langchain.schema import Document
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from utils.llm import get_model
from utils.logging import logger


class VerificationReport(BaseModel):
    """
    Structured verification report model.
    """
    supported: Literal["YES", "NO"] = Field(
        default="NO",
        description="Whether the answer is supported by the context"
    )
    unsupported_claims: List[str] = Field(
        default_factory=list,
        description="List of unsupported claims in the answer"
    )
    contradictions: List[str] = Field(
        default_factory=list,
        description="List of contradictions found in the answer"
    )
    relevant: Literal["YES", "NO"] = Field(
        default="NO",
        description="Whether the answer is relevant to the question"
    )
    additional_details: str = Field(
        default="",
        description="Additional details or explanations about the verification"
    )

class VerificationAgent:
    def __init__(self):
        base_model = get_model(max_completion_tokens=1200, temperature=0.0)
        # Use structured output to get VerificationReport directly
        self.model = base_model.with_structured_output(VerificationReport)
        logger.info("Mode lInference initialized successfully.")

    def generate_prompt(self, answer: str, context: str) -> str:
        """
        Generate a structured prompt for the LLM to verify the answer against the context.
        Note: The VerificationReport schema is automatically included via with_structured_output(),
        so we don't need to specify the format in the prompt.
        """
        prompt = f"""
        You are an AI assistant designed to verify the accuracy and relevance of answers based on provided context.

        **Instructions:**
        - Verify the following answer against the provided context.
        - Check for:
        1. Direct/indirect factual support (YES/NO)
        2. Unsupported claims (list any if present)
        3. Contradictions (list any if present)
        4. Relevance to the question (YES/NO)
        - Provide additional details or explanations where relevant.

        **Answer:** {answer}
        **Context:**
        {context}
        """
        return prompt

    def check(self, answer: str, documents: List[Document]) -> Dict:
        """
        Verify the answer against the provided documents.
        Returns a dictionary of verification result and used context.
        """
        logger.info(
            f"VerificationAgent.check called with answer='{answer}' and {len(documents)} documents."
        )

        # Combine all document contents into one string without truncation
        context = "\n\n".join([doc.page_content for doc in documents])
        logger.info(f"Combined context length: {len(context)} characters.")

        # Create a prompt for the LLM to verify the answer
        prompt = self.generate_prompt(answer, context)
        logger.info("Prompt created for the LLM.")

        # Call the LLM to generate the verification report
        try:
            logger.info("Sending prompt to the model...")
            verification_report: VerificationReport = self.model.invoke([HumanMessage(content=prompt)])
            logger.info(f"Verification report received:\n{verification_report}")

        except Exception as e:
            logger.error(f"Error during model inference: {e}")

            verification_report = VerificationReport(
                supported="NO",
                unsupported_claims=[],
                contradictions=[],
                relevant="NO",
                additional_details=f"Error during verification: {str(e)}",
            )

        return {
            "verification_report": verification_report,
            "context_used": context,
        }