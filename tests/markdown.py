answer="""
The case is a **British Columbia family law parenting dispute** (K.A.M. v. A.F.V., 2025 BCSC 427) about **parenting responsibilities and travel arrangements for an 11‑year‑old child**, particularly:

- **Whether and how often the father (respondent) can take the child from British Columbia to Washington State during his parenting time**, and whether the court should make a **non-removal / travel-restriction order** under **s. 64 of the Family Law Act (FLA)**.
- **Renewal and control/availability of the child’s travel documents**, including the child’s **U.S. passport** and **Nexus card**, and related cooperation between the parents.

Key factual and procedural features from the context:
- The claimant (mother) sought orders to **prevent removal of the child from B.C. without both parents’ consent or a court order**, or alternatively to **limit Washington travel to one weekend per month**, with notice and no missed school.
- The respondent (father) cross-applied for orders giving him control over **passport applications**, requiring the claimant to **cooperate in renewing the child’s U.S. passport**, and requiring delivery of the child’s **Nexus card** to him (to be held in trust).
- The court dealt with an application to **adduce late affidavit evidence after submissions**, relating to a “**School Incident**” where the father **unilaterally de-registered the child from her B.C. school and registered her in online school**, which the court found relevant mainly to context/credibility.
- The hearing was adjourned to obtain a **Views of the Child Report** by **Dr. Elterman**, which reported the child:
  - enjoys school and activities in **British Columbia** and has friends there;
  - does not want to spend more time in Washington;
  - would prefer **Washington trips “once every four weeks”**;
  - said her father tried to move her to remote schooling, which she did not want.

Orders/outcomes described in the context:
- The court **declined** to give the father **sole parental responsibility** for applying for passports (parents share responsibilities).
- The court ordered the claimant to **provide consent/signature to renew the child’s U.S. passport**.
- The court ordered the claimant to **provide the child’s Nexus card to the respondent**, but required that **travel documents be available to both parents** for necessary travel.
- The court **did not make a blanket order** requiring consent for any removal from B.C., but **limited the father’s travel outside B.C. with the child during the school year to one weekend every four weeks** (excluding holidays/vacations), based on the **child’s best interests** (stability, schooling, wellbeing, and the child’s expressed views), and required **advance notice** of any travel outside B.C. by either parent.'
"""
import gradio as gr

answer2 = f"""
    ## Answer 
    
    {answer}
"""


with gr.Blocks() as demo:
    with gr.Tab("Answer1"):
        gr.Markdown(answer)
    with gr.Tab("Answer2"):
        gr.Markdown(answer2)

if __name__ == "__main__":
    demo.launch()
