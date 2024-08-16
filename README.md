# Classification of PDFs from Web URLs

To run a template for GitHub:

1. **Clone the repository**: 
   ```bash
   git clone [<repository_url>](https://github.com/bindusri0702/Parspec_Assignment)
   ```

2. **Navigate to the project directory**:
   ```bash
   cd [<project_directory>](Parspec_Assignment/flask_app/)
   ```

3. **Install the required dependencies** using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run your application or script** as specified in your project’s documentation. For example:
   ```bash
   python deep.py
   ```

This should set up and run the template locally.


The process involved 90 minutes for data retrieval from web PDFs, followed by 120 minutes dedicated to preprocessing and applying a brute force classification approach. An additional 120 minutes were spent on machine learning model classification and Flask app development. Overall, the entire workflow, from initial planning to complete model building, was completed in under 6 hours.

. PDFs were read from the provided URLs.
2. The retrieved data was cleaned by retaining only alphabetic characters and spaces. Words shorter than four characters that are stopwords, image unicodes, and table elements, were removed.
3. PDFs that failed to render properly, such as those with request timeout errors, HTTP errors, or PDFs where the text was displayed as an image, were identified and removed.
4. Rows with no text, resulting from invalid URLs, were discarded.
5. Classification of PDFs was performed using the following methods:

   a) **Brute Force Approach**:
   - **Assumption**: It was assumed that each PDF primarily discusses the product it describes, so relevant product-related words are expected to appear more frequently.
   - **Supervised Task**: Labeled data indicating the correct product categories for each PDF was utilized.
   - **Stemming Words**: Each word in the PDFs was converted to its root form using stemming, ensuring consistency in the analysis.
   - **Count Word Occurrences**: A counter was used to tally the occurrences of each word's root form in each PDF.
   - **Label Frequency Analysis**: The frequency of product-related labels was analyzed by counting the occurrences of these labels in their root forms.

   This approach utilized word frequency to predict the product described in each PDF, performance of the model aligns well with the assumption that more frequent words are more likely related to the product.

   b) **Machine Learning Models**:
Machine learning models, from the simpler KNeighborsClassifier to more complex ones like RandomForestClassifier and GradientBoostingClassifier, were used for PDF classification. However, the performance results suggest that the simpler KNN outperforms RF and GB, as the latter models tend to overfit and fail to generalize well on testing samples.
There are three primary approaches to solving the classification of PDFs: logical heuristics, machine learning models, and deep learning models, each with its unique methodology and considerations.

1. **Logical Heuristics Approach**: This approach relies heavily on a deep understanding of the data to manually construct rules for classification. Since you are creating the rules based on your knowledge of the data, you have full control and a clear understanding of how the model works. This approach is transparent and interpretable, as every decision made by the model is based on rules you explicitly defined.

2. **Machine Learning Models**: Here, the focus shifts to building features from the PDF documents that will be used by the classification models. The effectiveness of these models largely depends on the quality and relevance of the features you create. The better and more detailed the features, the better the model's performance. However, unlike the logical heuristics approach, machine learning models require careful tuning and validation to avoid issues like overfitting and to ensure they generalize well to new data.

3. **Deep Learning Models**: In this approach, feature extraction is handled automatically by the model itself. You don't need to explicitly define features; instead, the model learns patterns and representations directly from the data. The performance of deep learning models is influenced by the complexity of the patterns in the data and the amount of data available. They can capture intricate patterns that might be missed by simpler models, but they also require large datasets and significant computational resources. Additionally, the inner workings of deep learning models are often less interpretable, making it harder to understand how they arrive at their decisions.
In this case, both logical heuristics and machine learning models were explored and compared. However, deep learning models were not pursued because they typically require larger datasets and well-structured, syntactically and semantically coherent sentences for effective training. This level of data quality is often lacking in product manuals, making deep learning less suitable for this specific task.
In logical heuristics approach 19 documents are being misclassified by the rules built, when validated it is found that most of these documents doesn’t have the product name specified in the entire PDF or it is not in the textual format that can be read. Sometimes PDFs that should be classified as “others” are misclassified into lighting, cable or fuses, because the PDFs appears to be using more of these words while describing product.
After careful analysis of misclassified PDFs, it is found that word “Lamp” is used as an alias to “lighting” in many PDFs, so this rule is also used in classification task. Similarly we can construct complex rules to categorise the PDF documents, in such a way they don’t overfit the model.
Accuracy is chosen to evaluate models, firstly because the data is almost balanced, secondly the cost of false positives is same as cost of false negatives in this case.



