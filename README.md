# irrelevant-youtube
Ranking comments based on relevancy to the video using NLP

## Relevance of Youtube Comments ranking pipeline implementation
1. Pre-trained BERT model on youtube comments dataset for improved accuracy.
2. Fine-tuned on multi-class relevance classification task
3. Utilised Sentence-Transformer re-ranking pipeline comprising of Bi-encoder and Cross-encoder for ranking the relvant comments.

## Experimentation
* Experimented without pre-training. Robert performed the best, then DistillBert and then Bert-base-uncased. Next step is to pre-train roberta and using it for fine-tuning.
* Experimented with data augmentation with paraphrasing using humarin/chatgpt_paraphraser_on_T5_base model for increasing samples of classes with very less data. Didn't get good results. Need to explore more.
* Will look to include video title and description as features in relevance classification task to provide some context to the model.

