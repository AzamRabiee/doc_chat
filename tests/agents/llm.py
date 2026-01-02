import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from langchain_core.messages import HumanMessage

from utils.llm import get_model

prompt = """
        You are an AI assistant designed to provide precise and factual answers based on the given context.

        **Instructions:**
        - Answer the following question using the provided context.
        - Be clear, concise, and factual.
        - Return as much information as you can get from the context.

        **Question:** What is the case about?
        **Context:**
        - [122] The Vehicle Lawsuits have spawned an expanding array of related and partially duplicate abusive litigation, including the Lawyers Lawsuit , the Family Lawsuit , the Expert Lawsuit , and the Insurer Lawsuit ( Bains v Day #1 ; Bains v Day #2 ). These matters largely represent a collateral attack on the findings in Bains v Adam #4 , and as previously noted, offend the prohibition against multiple tort actions in Cahoon v Franks , [1967] SCR 455. In the case of the Family Lawsuit , Acting Chief Justice Nielsen concluded that proceeding was being used as a proxy collateral attack action intended to circumvent resolution of the Vehicle Lawsuits . I also find as fact that filing the Family Lawsuit was an attempt to circumvent the case management structure imposed by the Court with respect to the Vehicle Lawsuits .
- [123] This pattern has now escalated outside of court litigation to attempts by Dr. Bains to trigger and/or conduct criminal proceedings against opposing parties and Justices of this Court. Expanding patterns of litigation and related activities are a particularly strong justification to impose prospective court access restrictions: Unrau #2 at paras 633-645.

[26] Under Rules 10-6(6) and 10-6(7) of the Supreme Court Family Rules , B.C. Reg. 169/2009 [ Rules ], an applicant is required to serve a copy of each filed affidavit mentioned in the notice of application on the respondent at least 8 business days before the hearing date. Pursuant to Rule 10-6(13) of the Rules , additional affidavits may only be served with the consent of all parties or by court order: Hudema v. Moore , 2020 BCSC 587 at para. 48, citing Quigg v. Quigg , 2019 BCSC 628.
[27] However, this is not simply a case of an affidavit being filed late, or of evidence sought to be adduced during the course of a hearing such as in Hudema and Quigg .
[28] The somewhat unusual aspects of this case are that it relates to events that were unknown to the claimant on the dates of the hearing, September 3 and 4, 2024, and the evidence sought to be adduced was filed after the completion of submissions on September 4, 2024, but before the Court's receipt of Dr. Elterman's Views of the Child Report. The Court left it open at the completion of the hearing on September 4, 2024 to potentially hear further submissions from the parties following completion of the Report, at the Court's discretion.
[29] The case law distinguishes between affidavits filed at different times, for example before the hearing commences; once submissions have already
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 7
commenced; after submissions are completed and the decision is under reserve; and after judgment but before an order has been entered.
- [30] At the hearing on October 3, 2024, the Court referred to Victoria and District Cricket Association v. West Coast Cricket Organization , 2024 BCSC 65 [ Victoria Cricket Association ], for its potential application in the circumstances.
- [31] In that case, the parties disagreed on the appropriate test to be applied where the petitioners brought an application to have a new affidavit entered into evidence on the second day of a hearing which occurred after a two-month break in the proceeding. The parties' positions were summarized by Justice Shergill as follows:
- [16] Counsel for the Petitioners submits that the appropriate test to be applied to admit the Gupta Affidavit is set out in Rosenstein v. Atlantic Engraving Ltd., 2002 FCA 503, at para. 8, where the Court held that late-filed affidavits could be admitted into evidence if the following requirements were met: (a) the evidence adduced will serve the interests of justice; (b) the evidence will assist the court; and (c) the evidence will not cause substantial or serious prejudice to the opposing party. I note that at para. 9, the Court adds a fourth element-that the party seeking leave to file the additional affidavit material must show that the evidence sought to be adduced was not available prior to the date on which it was due.
- [17] The Respondents characterize this application to adduce additional affidavit evidence as a request to 'reopen' the Petitioners' case. Consequently, they submit that the appropriate test to be applied is that articulated by the Court in Palmer v. The Queen , [1980] 1 S.C.R. 759, 1979 CanLII 8 at 775, for the admission of evidence that existed at the time of trial but was not presented in court.
- [18] The Palmer test provides as follows: (a) the evidence should generally not be admitted if, by due diligence, it could have been adduced at trial provided that this general principle will not be applied as strictly in a criminal case as in civil cases; (b) the evidence must be relevant in the sense that it bears upon a decisive or potentially decisive issue in the trial; (c) the evidence must be credible in the sense that it is reasonably capable of belief; and (d) the evidence must be such that if believed it could reasonably, when taken with the other evidence adduced at trial, be expected to have affected the result.
- [19] While conceding that the discretion to admit new evidence is wider on an interim application then on the final order on appeal (see Can-West Development Ltd. v. Parmar, 2018 BCSC 1716 at para. 12), the Respondents submit that the general principles laid out in Palmer still apply to the circumstances of this case.
- [20] I do not agree that the Gupta Affidavit Application is similar to a request to reopen the Petitioners' case. The Petitioners' case was still open when the Gupta Affidavit Application was brought, and Mr. Sheikhupura had not finished his main submissions on the Disqualification Application. As such, the factors in Palmer do not have direct application to this case.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 8
[21] In First National Financial GP Corporation v. 0734763 B.C. Ltd. , 2020 BCSC 1349 (' First National '), counsel sought to rely on Palmer in circumstances where the application to adduce further evidence was brought after submissions were completed but while the matter was under reserve. In rejecting the argument that the Palmer test applied, Master Elwood (as he then was), held as follows:
- [58] The full Palmer test, which is generally applied on appeals, does not apply to evidence which is submitted to the court for consideration while an application such as this is under reserve. That being said, the rule against splitting one's case applies to applications as well as trials. As a general rule, an applicant should not be permitted to split his or her case by leading evidence by way of a supplementary affidavit which the applicant should have known would be necessary to counter a position advanced during the hearing: Ulrich v. Ulrich , 2004 BCSC 95, at para. 42-43 and 45.
[59] Moreover, Rule 8-1(14) prohibits additional affidavit evidence following the deadline for reply affidavits without leave of the court. Although the court has discretion to consider further evidence prior to judgment, that discretion should be exercised sparingly to avoid an injustice: Ivarson v. Lloyd's M.J. Oppenheim Attorney In Fact In Canada for Lloyd's Underwriters et al, 2002 BCSC 1627 at para. 25; Muller v. Muller, 2015 BCSC 370, at para. 15.
[Emphasis added.]
[32] Ultimately, Shergill J. decided that the test to be applied was one where the hearing had already commenced, but before the hearing has concluded, as follows:
[28] The jurisprudence leads me to conclude that the exercise of the court's discretion to admit affidavit material filed after a hearing has already commenced, but before the hearing has concluded, requires the court to balance the interests of 'truth-seeking, fairness, and prejudice'. This balancing exercise should be done having regard to the following non-exhaustive factors:
- 1. the relevance of the evidence to the issues before the court;
- 2. the necessity or importance of the evidence to deciding the issues;
- 3. whether the evidence is reasonably capable of belief;
- 4. the timing of the application;
- 5. whether the evidence existed prior to the commencement of the hearing;
- 6. the explanation for the delay in providing the evidence;
- 7. whether there is any prejudice to the opposing party by the late admission of the evidence; and
- 8. whether any prejudice can be mitigated by, for example, permitting the objecting party to file responding affidavits and/or make additional submissions, or the making of a costs award.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 9
[33] Here, when the claimant applied to adduce new evidence, submissions had been heard on the claimant's application and the respondent's cross-application, but further evidence was intended to be received by the Court in the form of Dr. Elterman's Views of the Child Report, and the Court had left open the possibility of further submissions on that Report.
[34] A close parallel is the Victoria Cricket Association decision of Shergill J., where the hearing has already commenced, but before the hearing had concluded.

[90] In a notice of application filed August 19, 2024, the respondent seeks the following orders:
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 21
- 1. An order that the respondent will have sole parental responsibilities in relation to applying for any and all passports for the Child;
- 2. An order that the claimant will cooperate with the respondent to renew the Child's U.S. Passport;
- 3. An order that the respondent shall inform the claimant if any further steps are necessary to complete the Child's U.S. Passport renewal;
- 4. An order that the respondent shall hold the Child's U.S. Passport in trust for the Child; and
- 5. An order that the claimant shall deliver the Child's Nexus card to the respondent, to be held in trust for the Child.
[91] The respondent's evidence is that the claimant has frustrated his attempts to obtain the claimant's consent to review the U.S. Passport, and had refused to provide the Child's Nexus card to him, despite his request for it to ease the Child's crossing from Canada to the United States, particularly during peak seasons.
[92] The claimant's evidence is that the Nexus card is under her application and she uses it for travel with the Child. The claimant does not explain how often she makes use of the Nexus card for travelling with the Child.
[93] The claimant submits that she did not sign an application to renew the Child's U.S. Passport because the respondent provided her with an incomplete document.
[94] In her application response, the claimant states that she agrees the Child should maintain both Canadian and U.S. passports because she is a dual citizen of both nations.
[95] I understand the parties have agreed that the respondent is to hold the Child's U.S. Passport in trust for the Child, and the claimant is to hold the Child's Canadian Passport in trust for the Child.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 22
[96] Pursuant to an Order of Justice Hori, dated August 16, 2023, the parties share parental responsibilities. Under s. 41 of the FLA , parental responsibilities include 'applying for a passport, licence, permit, benefit, privilege or other thing for the child.'
[97] The claimant cites T.L.M. v. J.K.B ., 2018 BCSC 2237 where one of the issues was a Nexus card. I did not find the case useful regarding the Nexus card as it refers to the terms of the trial judge's order regarding possession of the Nexus card, without stating what those terms are; however, the case is useful in Justice Weatherill's comments that in fairness, if the father is thinking of about what is in the child's best interests, he should give as much advance notice to the mother of travel plans involving the child. Those comments apply equally well to both parents in the case at bar.
[98] In Pasco , the claimant applied for an order requiring the respondent to execute a general travel authorization to permit her to travel with the child for up to 24 hours, including the United States, and to provide his written consent to enroll the child in the Nexus Trusted Traveller Program.
[99] Justice Skolrood (as he then was) made the following comments regarding the court regulating the conduct of the parties, which are equally appropriate for the case at bar, as follows:
- [11] It is apparent from reviewing the affidavit material filed on the application that the parties continue to have considerable difficulty communicating and cooperating with respect to the parenting of the child. There is a clear lack of trust that runs through the correspondence between them and a tendency to involve counsel on matters that should reasonably be resolved by the parents. That includes the matters that are the subject of this application.
- [12] I make the further observation that while it is obviously open to either of the parties to bring applications before the court, the court is limited in what it can do in terms of regulating the conduct of the parties. The only people who can ensure the type of cooperation and flexibility that is necessary to promote the best interests of the child are the parties themselves, and they need to start figuring out how to do so before lasting harm is done to the child from their ongoing animosity.
- [13] Turning to the first order sought by the claimant for a general 24-hour travel authorization, I agree with the respondent that this amounts to a variation of the final order in that it would eliminate the need for the other parent to consent to travel.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 23
- [14] That said, and despite what I observed previously about the ability of the court to regulate the parties' conduct, the court should look for ways to reduce rather than increase opportunities for conflict. Court orders governing parenting time and parenting responsibilities should also provide parents with some flexibility during their parenting time to engage in activities with their child without being subject to an effective veto by the other parent. With that in mind, and perhaps with the benefit of some hindsight, I think the requirement for consent from the other parent for travel of less than 24 hours is overly restrictive.
- [15] I therefore order that s. 10 of the final order will be varied to provide that each parent will execute a general consent for travel of up to 24 hours, including travel to the United States. However, it is only fair and reasonable that the travelling parent give the other parent 24 hours' notice of proposed travel, including date, time and destination. That notice is for the purpose of keeping the other parent informed, but not for the purpose of requiring consent. I would add that such travel is only permitted during that parent's scheduled parenting time.
[Emphasis added.]
[100] In Pasco , regarding the Nexus pass, Skolrood J. responded to the respondent questioning the court's jurisdiction to compel a parent to sign a Nexus application by referring to ss. 41, 42 and 45 of the FLA regarding parenting responsibilities, concluding that it was in the child's best interests to obtain a Nexus card as a matter of convenience to reduce travel and waiting time: see Pasco at paras. 19-29.
- [101] Justice Skolrood concluded his discussion on the issue with the following pointed comment about the role of the court:
- [28] I come to this conclusion with some reluctance because, as I alluded to earlier and as I indicated to counsel, my view is that it is not the role of the court to involve itself in everyday parenting decisions. That fundamentally is the role of the parents.
- [29] Nonetheless I am prepared to order that the respondent execute an authorization to enroll the child in Nexus in the form required by the relevant authorities.
[102] Similarly here, to facilitate the exercise of parenting responsibilities and the Child's travel, I make an order that the claimant provide her consent and signature for the purposes of renewing the U.S. Passport.
[103] Regarding the Nexus card, from the evidence on this application, the respondent can make use of the Nexus card for the purpose of facilitating the Child's travel across the border.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 24
[104] As a result, I make an order that the claimant provide the Child's Nexus card to the respondent, but the Child's travel documents, including but not limited to the Nexus card, the U.S. Passport and the Canadian Passport, must be available to both parents for the purpose of any travel requiring the use of the documents, or for facilitating such travel.
[105] I need not make any factual determinations about the various allegations about the conduct of the parties relating to the Child's travel documents. There appears to be agreement between the parties about the respondent holding the U.S. Passport and the claimant holding the Canadian Passport.
[106] I decline to vary the allocation of parental responsibilities by granting the respondent sole responsibility for applying to any and all passports for the Child. The parties share these responsibilities and must work together to exercise them in the best interests of their Child.

[35] Referring to the factors to be considered from the Victoria Cricket Association case, the evidence of the School Incident is relevant to the claimant's application and the respondent's cross-application because the hearing was not wholly concluded pending receipt of Dr. Elterman's Report, and the Report includes a reference to the School Incident.
[36] Since the Report is before the Court, and refers to the School Incident, it would be artificial to not consider the evidence relating to the School Incident in this application; however, the reference to the School Incident in the Report relates primarily to the Child's views on schooling.
[37] The Report is also relevant to credibility, although because the application and cross-application are interim applications based on affidavit evidence, consideration of credibility is limited. Here, the issue of credibility primarily arises in the context of the timing of the School Incident in relation to some of the respondent's submissions at this hearing.
[38] I find it disingenuous on the part of the respondent that on September 4, 2024, at virtually the same time that the respondent was unilaterally de-registering the Child from the School, his counsel was making the following written submissions to this Court critically accusing the claimant of making unilateral decisions in exercising her parental responsibilities for the Child, and contrasting his own purported communicative and cooperative behaviour, as follows:
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 10
- 11. In contrast, the Respondent has consistently involved the Claimant in his exercise of parental responsibility for [the Child]. He endeavours to include the Claimant and cooperate with her regarding all matters concerning [the Child].
…
- 97. The Respondent is gravely concerned about the Claimant's approach to coparenting, in particular the Claimant's lack of effective communication as well as her exclusion of the Respondent from important decisions and matters concerning [the Child].
[39] Again, at virtually the same time that the respondent's counsel was making those submissions in this Court, the respondent was de-registering the Child from the School, and two months prior, on July 6, 2024, without notice to the claimant, he had taken steps to register the Child in the online school.
[40] I note that I am not critical of respondent's counsel in the absence of any evidence that counsel was aware of the respondent's actions regarding the School Incident at the time.
- [41] I note also that the respondent's counsel's submissions on September 4, 2024 included the allegation that the claimant's application is 'clearly an attempt to shore up her own legal position'. A reason for her request for this order is because, as she asserts, the 'Respondent appears to be trying to deceptively build a case for relocation.'
[42] The events of the School Incident appear to provide support for the claimant's suspicions about the respondent's intentions; however, as will be seen below, the claimant's concerns about relocation are not a factor in my decision on the claimant's application to limit the frequency of travel to Washington during the school year, nor on the respondent's cross-application regarding travel documents.
[43] Returning to the test for re-opening a hearing to admit new evidence, regarding the necessity or importance of the evidence to deciding the issues before the Court, I find that the new affidavits are not necessary or of importance to a proper determination of the issues on the claimant's application and respondent's cross-application, but they do provide some useful context for the respondent's credibility and his critical submissions alleging that the claimant makes unilateral
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 11
decisions, and also the respondent's position taken at the hearing that evidence of the respondent having taken the Child to visit a school in Washington was inadmissible as hearsay, while not denying that he had done so.
[44] On the third factor, the evidence is reasonably capable of belief in that the respondent does not deny having de-registered the Child from the School, and responds to the claimant's affidavit with his own affidavit admitting to his registering the Child in the online school.
[45] Regarding the timing of the application, the claimant sought the application in a timely manner after having applied to the Court on short notice on October 6, 2024 to have the Child re-registered in the School, followed by the application to have the evidence of the School Incident heard in this application.
[46] The evidence of the School Incident was not available at the time of the hearing because it was occurring on the very day of the hearing, the respondent having taken steps to de-register the Child from the School without notice to the claimant. The claimant did not delay in making this application.
[47] I find that admitting the affidavit would not cause significant additional prejudice to the respondent, and the respondent has filed an affidavit in response to the claimant's affidavit.
[48] Overall, it is in the interests of justice to admit the evidence in the claimant's and respondent's affidavits. As a result, I have considered the contents of the affidavits in considering the issues on the claimant's application and respondent's cross-application; however, the evidence regarding the School Incident is of limited relevance to the issues.

[49] The next issues to be decided are the claimant's application for orders to prevent or limit the respondent taking the Child to Washington during his parenting time without the claimant's consent; and the respondent's cross-application for
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 12
orders relating to the renewal of the Child's United States passport and availability of the Child's Nexus card to the respondent.
[50] The hearing on September 4, 2024 was adjourned pending the parties retaining Dr. Elterman to conduct an interview of the Child as he saw fit for the purpose of his preparation of the Views of the Child Report.
- [51] The resulting Report is dated October 30, 2024. Select contents of the Report are summarized as follows:
- a)  Dr. Elterman is a Clinical and Forensic Psychologist. In preparing his report, Dr. Elterman interviewed the Child on September 17, 2024 and October 4, 2024;
- b)  Dr. Elterman reports that the Child told him that she enjoys attending school in British Columbia and that she is involved in activities there. She stated that she is on a soccer team, has trampoline lessons, and goes to gymnastics twice a week;
- c) The Child said she has friends in British Columbia, who she misses when she is in Washington. She also spoke about one friend in Washington;
- d)  The Child told Dr. Elterman that she does not mind the five-hour drive to Washington but that she does not want to spend more time there;
- e)  The Child told Dr. Elterman that her father tried to take her out of her school in British Columbia and put her in a remote school. She told him she did not want to do that and that she likes going to school in British Columbia;
- f) When asked about how often she goes to Washington, the Child said that she would like to go once every four weeks and that this would be 'just right';
- g)  Dr. Elterman concludes that the Child's view regarding trips to Washington is that 'she would want to go down for one weekend a month but otherwise wants to live in [British Columbia].'
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 13
[52] The claimant seeks an order pursuant to s. 64(1) of the FLA that the Child not be removed from British Columbia without both parties' consent or a court order. In the alternative, she seeks an order that the respondent's travel with the Child be limited to one weekend per month (two nights), provided that the Child does not miss any school and the respondent shares the details of the travel with the claimant.
[53] The claimant also seeks an order that the respondent transfer the Child's passports to the claimant's counsel, if the Court is satisfied that the respondent intends to remove the Child from British Columbia.
[54] Under s. 64 of the FLA , the Court has the power to make orders preventing the removal of a child from a specific geographic area, as follows:
- 64 (1)  On application, a court may make an order that a person not remove a child from a specified geographical area.
- (2) On application, if satisfied that a person proposes to remove a child from, and is unlikely to return the child to, British Columbia, the court may order the person who proposes to remove the child to do one or more of the following:
- (a) give security in any form the court directs;
- (b) surrender, to a person named by the court, passports and other travel records of the person who proposes to remove the child or of the child, or of both;
- (c) transfer specific property to a trustee named by the court;
- (d) if there is an agreement or order respecting child support, pay the child support to a trustee named by the court.
- (3) This section does not apply in relation to the relocation of a child within the meaning of Division 6 [Relocation] of this Part.
- (4) A person required by an order made under this section to hold passports, travel records or other property delivered under the order must do so in accordance with the directions set out in the order.
[55] Section 222 of the FLA provides that the court may make an order under Division 5 - Orders Respecting Conduct for one or more of the following purposes:
- (a) to facilitate the settlement of a family law dispute or of an issue that may become the subject of a family law dispute;
- (b) to manage behaviours that might frustrate the resolution of a family law dispute by an agreement or order;
- (c) to prevent misuse of the court process;
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 14
- (d) to facilitate arrangements pending final determination of a family law dispute.
[56] Section 227 of the FLA provides that the court may make an order requiring a party to do one or more of the following:
- (a) give security in any form the court directs;
- (b) report to the court, or to a person named by the court, at the time and in the manner specified by the court;
- (c)  do or not do anything, as the court considers appropriate, in relation to a purpose referred to in section 222.
[57] In Law v. Cheng , 2015 BCSC 1607, the claimant applicant sought an order pursuant to ss. 64(1), 222, and 227 of the FLA that the respondent not remove the parties' child from the Lower Mainland of British Columbia during her parenting time except in compliance with an Order previously made at a Judicial Case Conference ('JCC Order'), which provided that neither party would remove the Child's permanent residence from the Lower Mainland of British Columbia without the written consent of the other party, or a court order.
[58] The evidence was that the parties shared parenting time with the child, alternating one week on, one week off. The respondent had been taking the child to Toronto on her parenting time. The respondent had notified the claimant of her intention to do so, with details of dates, flights, and destination, but the claimant had objected to the travel on the basis that the child would be subjected to unnecessary travel and he would be suffering from jet lag which was unhealthy and not in his best interests. There was no suggestion that the respondent did not intend to return to British Columbia with the child.
[59] The Court found that in breach of the JCC Order the respondent had effectively moved the child's residence during her periods of parenting, contrary to the JCC Order, and further, the Court found that the evidence supported that the frequent travel and the time during which he travelled was not in the best interests of the child given the effect on him and on his health.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 15
[60] As a result, the Court granted the requested order pursuant to ss. 64(1), 222, and 227 of the FLA that the respondent shall not remove the child from the Lower Mainland of British Columbia during her parenting time, except with written consent of the other party, or a court order, which was consistent with the original JCC Order, a distinguishing feature from the case at bar.
[61] Section 64(1) provides broad authority to the court on an application for an order that a person not remove a child from a specified geographical area, without qualification.
[62] Section 64(2) applies to an application where the court is satisfied that a person's propose is to remove a child from, and is unlikely to return the child to British Columbia.
[63] In J.Z. v. L.H.C. , 2015 BCSC 97, at para. 14, the Court referred to s. 64 of the FLA , without distinguishing between sub-sections (1) and (2) of that section, observing that to issue a non-removal order, the court must be satisfied that a person proposes to remove a child from, and is unlikely to return the child to British Columbia. In my view, J.Z. can be distinguished on that basis as no distinction is made between sub-sections (1) and (2) of s. 64.
[64] Also, I note that s. 64 of the FLA governs removal, as distinguished from relocation, which is 'a change in the location of the residence of a child or child's guardian' that can reasonably be expected to significantly impact on the child's relationship with a guardian or other persons who play a significant role in the child's life: FLA, s. 65.
[65] The respondent argues that an order restricting travel is not necessary because both Canada and the United States are signatories to the Convention on the Civil Aspects of International Child Abduction, 25 October 1980, Can. T.S. 1983, No. 35 (the ' Hague Convention ').
[66] The respondent cites Silva v. Salanova , 2012 BCSC 1787 as an example of a case in which the Court found it appropriate to grant leave for a mother to travel with
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 16
her children to Brazil during the summer, in part because the Hague Convention 'provides remedies … if [the mother] defies this court order and does not return the boys to Vancouver': Silva at para. 31.
[67] I accept that the Hague Convention could provide remedies if the respondent wrongfully relocated the Child to the United States; however, I do not find this particularly helpful in making a determination on the facts before me, as there has not been a concern voiced that the respondent intends to take the Child to Washington and not return the Child to British Columbia. The respondent has frequently travelled with the Child to Washington and returned with her to British Columbia.
[68] While I agree that the respondent's behaviour, including the frequent visits to Washington and the School Incident, suggest he is trying to foster connections between the Child and Washington which may factor in his stated intention to relocate the Child to Washington, the respondent's travel to Washington every weekend during his parenting time, that is, twice a month, does not support an order pursuant to s. 64 preventing the removal of the Child from British Columbia; however, while I decline to make an order preventing the Child from being removed from British Columbia without qualification, I consider it appropriate to limit the respondent from removing the Child from British Columbia under s. 64 of the FLA , for the reasons discussed below in consideration of the best interests of the Child, other than one weekend of the respondent's parenting time, out of every four weekends, while the Child is in school, other than school vacations or school holidays.
[69] As noted above, the claimant and respondent share parental responsibilities and parenting time. Pursuant to s. 41 of the FLA , parental responsibilities include making day-to-day decisions affecting the child and having day-to-day care, control and supervision of the child, making decisions respecting where and with whom the child will live, and making decisions respecting the child's education and participation in extra curricular activities. During parenting time, a guardian may
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 17
exercise the parental responsibility of making day to day decisions affecting a child, subject to any agreement or order: FLA, s. 42.
[70] Under s. 45 of the FLA , the Court may make an order respecting parental responsibilities or parenting time.
- [71] In making an order respecting parenting arrangements, the best interests of the child are the only consideration for the Court: FLA , s. 37. Under s. 37(2), the factors to consider when determining the best interests of the chid include: the child's health and emotional well-being; the child's views; and the child's need for stability, given the child's age and stage of development.
[72] Even though I have found that the respondent does not propose to remove the Child from British Columbia when he is unlikely to return her, I find that it is in the Child's best interests to make the order limiting the frequency of the travel back and forth between British Columbia and Washington during the school year.
- [73] The Views of the Child Report supports this conclusion. As Dr. Elterman reports, the Child has strong social connections to British Columbia, including friendships, her school community, and relationships forged through her various extracurricular activities. These relationships are important to the Child's emotional well-being and it is in her best interests to maintain them.
- [74] Under s. 37(2) of the FLA , to determine what is in the child's best interests, all of the child's needs and circumstances must be considered, including the factors set out in sub-paragraphs (a)-(j) of s. 37(2), including of relevance here: (a) The child's health and emotional well-being; (b) the child's views, unless it would be inappropriate to consider them; (d) the history of the child's care; and (e) the child's need for stability, given the child's age and stage of development.
[75] Regarding the Child's health and emotional well-being, there is some evidence that returning to British Columbia late in the evening impacts the Child's sleep schedule and schooling.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 18
[76] Regarding the Child's views, s. 37 of the FLA requires this Court to consider the views of the children with respect to parenting time unless it would be inappropriate to do so: see D.R. v. K.A ., 2022 BCSC 1257 at para. 37.
[77] Here, the parties agreed to jointly retain Dr. Elterman for the purpose of eliciting the Child's views, specifically with respect to the frequency and duration of travel to Washington. According to the Views of the Child Report, the Child expressed her views to Dr. Elterman on that topic.
[78] Selected quotes from Dr. Elterman's report regarding the Child's views on travel to Washington are as follows:
-  In response to his question to her how often she goes to Washington for the weekend:  'She says that she wants it to be once every 4 weeks. She says this would be 'just right''.
-  '[The Child] says that she does not mind the travel between [British Columbia] and [Washington] but she just doesn't want to spend more time in [Washington]. [The Child] said that she was fine with one weekend a month going down to her father's home in [Washington] during his week. During the other week she says that she would want to stay in [British Columbia]. She says that she does not mind the drive.'
[79] I find it appropriate to take the Child's views into account. Her views are not determinative of the issue, but carry some weight, given her current age, 11, and also Dr. Elterman's Report referring to the Child's preference for one weekend a month in Washington being consistent across parents and over time in saying this, and that her reasons were related to location and the activities that she would want to do in British Columbia.
[80] While the Child told Dr. Elterman that she is not bothered by the length of time it takes to travel to and from Washington, I also find that a 5-hour drive each way, for a total of approximately 10 hours of travel roundtrip, is a significant amount
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 19
of time for an 11-year-old to spend in the vehicle every other weekend, twice a month.
[81] I accept the respondent's evidence that the trips to Washington have not caused the Child to miss classes or her activities during the week, except that the claimant's evidence is that she has been late to school and missed homework from the late arrival in British Columbia from Washington. I accept that travelling for this length of time and distance two weekends each month impacts the Child's ability to adjust to the school week and affects her sleep. Taking into account the Child's need for stability given her age and development, I find that it is in her best interests to place some limits on her travel to Washington.
[82] I also consider it beneficial to both parents to be aware of where and when the Child travels outside British Columbia. For that reason, I am not at this time requiring the consent of both parents to travel, but advance notice of travel in terms of the dates of travel and destination must be communicated to the other parent for any travel by either parent with the Child outside British Columbia at any time.
[83] Given the above, I find it is in the Child's best interests to make an order pursuant to ss. 64(1) and 45 of the FLA limiting travel outside British Columbia during the respondent's parenting time to one weekend every four weeks while the Child is attending school, other than school holidays and vacation; the intention being that if the respondent has parenting time every other week, each week commencing mid-week, and he wishes to travel to Washington with the Child, he can do so on one of the two weekends he has parenting time with the Child within each four week span.
[84] The claimant's application refers to 'two overnights'; however, with statutory holidays resulting in three day weekends, and teachers' professional days often coinciding on weekends with statutory holidays, limiting the weekend to two overnights is overly restrictive for long weekends.
2025 BCSC 427 (CanLII)
K.A.M. v. A.F.V.
Page 20
[85] Given the claimant's expressed concern about the Child returning to British Columbia late in the evening before a school day, I have also considered a time limitation for the Child's return to British Columbia by before the Child's regular bedtime; however, travel schedules, border crossings and traffic can not always be controlled or anticipated with regularity; and, as noted in Pasco v. Pasco , 2016 BCSC 2484, discussed below, it is not the role of the court to involve itself in everyday parenting decisions, that being the role of the parents.
[86] Nevertheless, both parents are expected to be making everyday parenting decisions that are in the best interests of the Child, including travel decisions affecting the Child's health and well-being.
[87] The claimant also seeks orders that: a) the habitual residence of the Child shall remain in British Columbia; b) neither party shall change the habitual residence of the child; and c) neither party shall advise the Child of any potential changes in her habitual residence.
[88] I find it is unnecessary to make such orders at this time as the parties agree and the Court has previously found that the Child resides in British Columbia: Meik 2022 at paras. 20, 35.
[89] If either party wishes to relocate the Child from British Columbia, leading to a change in the location of her residence that can reasonably expected to have a significant impact on her relationship with the other guardian or other persons who play a significant role in her life, then they will be required to comply with the provisions for notice under s. 66 of the FLA and s. 16.9(1) of the Divorce Act . Failure to comply may result in further orders from the Court: see Nalinakshan v. Dileep , 2021 BCSC 2565 at para. 22.

        **Provide your answer below:**

"""


model = get_model(max_completion_tokens=1200, temperature=0.3)
print("Model Inference initialized successfully.")

response = model.invoke([HumanMessage(content=prompt)])
print("LLM response received.")
print("Content len=%s", len(response.content or ""))
print("additional_kwargs=%s", response.additional_kwargs)
print("response_metadata=%s", getattr(response, "response_metadata", None))
