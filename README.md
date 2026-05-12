# Presumed Heroes, Victims, and Villains

**Narrative framing analysis in news media using LLMs.**

`Python` · `DSPy` · `LLM-as-judge`

Two journalists cover the same protest. One writes: *"Blockades by activists create chaos in The Hague."* The other: *"Protests seek to bring focus to the climate crisis."* Same event, starkly different impression. This is framing: presentation and word choice shape how audiences understand the news. 

Many computational tools approach framing analysis by categorizing articles into topics (e.g. Economics, Public Safety, Morality). But that can flatten meaning: *"immigrants are taking our jobs"* and *"immigrants boost the local economy"* both get tagged as "Economics" despite eliciting opposite feelings. 


This project takes a different angle. News stories often carry an underlying narrative structure, with some actors implicitly framed as heroes, others as victims, others as villains. Indentifying these narrative roles offers a different lens for understanding how a story is being told.


Built with [DSPy](https://dspy.ai), a framework for building LLM pipelines by defining task structure rather than writing raw prompts by hand.

📄 [Read the paper](Narrative%20Framing%20Analysis%20with%20LLMs.pdf)

## Results

Zero-shot prediction with narrative arc signature and a few-shot LLM judge (vs. 30.26% zero-shot baseline for hero):

| Role    | Accuracy   |
|---------|------------|
| Hero    | **64.47%** |
| Villain | **66.67%** |
| Victim  | **60.71%** |

---

## Approach

**Predictor: joint narrative arc extraction.** An initial prompt asking directly "who is the hero?" biased the model toward individuals over organizations. Prompting the model to first identify the central conflict, then extract all three roles simultaneously, produced substantially better results.

**Judge: few-shot semantic matching.** Syntactic matching fails on paraphrases (*"California lawsuit"* vs. *"California and the coalition of states fighting for environmental protection"*). A few-shot judge with hand-picked examples, instructed to assess semantic similarity in the context of the article, corrected this.

---

## Data

The [Narrative Frame Corpus](https://github.com/phenixace/narrative-framing) by Frermann et al. (2023), released under an MIT license. It contains 428 manually annotated climate change articles from US and UK outlets, balanced across publication date (2017–2019) and four political leanings (left, center-left, right, questionable source) as classified by Media Bias Fact Check. Each article is annotated with entities and their narrative roles. A 25% hold-out test set was stratified by outlet leaning.

---

## Limitations

- **Abstention**: generative models almost always extract an entity even when no clear narrative role exists.
- **LLM bias**: models may project ideological assumptions onto role assignments rather than staying faithful to the text.
- **Reliability**: framing is inherently interpretive. Automated extraction can surface patterns, but a human-in-the-loop review process would be essential to build trust in deployment.

---

## References

- Frermann, L., Li, J., Khanehzar, S., & Mikolajczak, G. (2023). Conflicts, villains, resolutions: Towards models of narrative media framing. *ACL 2023*.
- Stammbach, D., Antoniak, M., & Ash, E. (2022). Heroes, villains, and victims, and GPT-3: Automated extraction of character roles without training data. *WNU 2022*.
