from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel  #to convert dict to runnables
from langchain_core.runnables import RunnableLambda


model = ChatMistralAI(model = "mistral-small-2506")
parser = StrOutputParser()


#Two different prompts 
short_prompt = ChatPromptTemplate.from_template(
    "Excplain {topic} in 1-2 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)


#Input
topic = "Machine Learning"

#Now if we want to create CHAIN then we will connect "Short_Prompt" to "Model" and connect "Model" to "Parser" and whatevwe output it gives, we will print it

#and for detailed_prompt, we will create a another pipeline

#BUT THE PROBLEM IS THAT FIRST PIPELINE WILL RUN, THEN NEXT PIPE LINE WILL RUN, BUT BOTH WILL NOT BE ABLE TO RUN AT ONCE simultaneously

# formatted_short = short_prompt.format_messages(topic = topic)
# response_short = model.invoke(formatted_short)
# str_out = parser.parse(response_short.content)


# formatted_detailed = detailed_prompt.format_messages(topic = topic)
# response_short = model.invoke(formatted_short)
# str_out = parser.parse(response_short.content)


#NOW ALSO IT WILL NOT BE PARALLEL  >> SO INSTED OF THESE WE CAN USE OUR PARALELL RUNNABLE

# SO FOR IT WE WILL HAVE TO CREATE PIPELINES 

#dictonary
# chain = {
# "short" : short_prompt | model | parser,
# "detailed" : detailed_prompt | model | parser
# }


#dictonary is not runnable we have to convert it to runnables first to invoke it 

#Converting dict to runnable parallel
# chain = RunnableParallel({
# "short" : short_prompt | model | parser,
# "detailed" : detailed_prompt | model | parser
# })


# result = chain.invoke({"topic" : "Machine Learning" })   #with it paralelly both pipeline will get executed


# print(result)
# print(result['short'])
# print(result['detailed'])







# Machine Learning (ML) is a branch of AI where algorithms learn patterns from data to make predictions or decisions without being explicitly programmed. It improves automatically with experience.
# ### **Machine Learning (ML) – A Detailed Explanation**

# Machine Learning (ML) is a subset of **Artificial Intelligence (AI)** that enables systems to **learn from data** without being explicitly programmed. Instead of following rigid rules, ML models **identify patterns, make decisions, and improve over time** by analyzing large datasets.

# ---

# ## **1. Core Concepts of Machine Learning**
# ### **1.1 What is Learning in ML?**
# - **Traditional Programming:** A programmer writes explicit rules (e.g., `if temperature > 30°C, turn on AC`).
# - **Machine Learning:** The system **learns the rules from data** (e.g., given historical temperature and AC usage data, the model predicts when to turn on the AC).

# ### **1.2 Key Characteristics of ML**
# - **Adaptability:** Models improve with more data.
# - **Generalization:** Works well on unseen data (if trained properly).
# - **Automation:** Reduces manual effort in decision-making.
# - **Scalability:** Can handle large and complex datasets.

# ---

# ## **2. Types of Machine Learning**
# ML is broadly categorized into **three main types**, based on the learning approach:

# ### **2.1 Supervised Learning**
# - **Definition:** The model is trained on **labeled data** (input-output pairs).
# - **Goal:** Predict the correct output for new inputs.
# - **Examples:**
#   - **Classification:** Spam detection (Spam/Not Spam), Image recognition (Cat/Dog).
#   - **Regression:** Predicting house prices, stock market trends.

# #### **Common Algorithms:**
# - Linear Regression
# - Logistic Regression
# - Support Vector Machines (SVM)
# - Decision Trees
# - Random Forest
# - Neural Networks

# ---

# ### **2.2 Unsupervised Learning**
# - **Definition:** The model learns from **unlabeled data** (no predefined outputs).
# - **Goal:** Find hidden patterns or groupings in data.
# - **Examples:**
#   - **Clustering:** Customer segmentation, anomaly detection.
#   - **Dimensionality Reduction:** PCA (Principal Component Analysis).

# #### **Common Algorithms:**
# - K-Means Clustering
# - Hierarchical Clustering
# - DBSCAN
# - Apriori Algorithm (for association rules)
# - Autoencoders (for deep learning)

# ---

# ### **2.3 Reinforcement Learning (RL)**
# - **Definition:** The model learns by **interacting with an environment** and receiving **rewards/penalties**.
# - **Goal:** Maximize cumulative reward over time.
# - **Examples:**
#   - Self-driving cars adjusting steering.
#   - AlphaGo (Google’s AI that beat human Go champions).
#   - Robotics (e.g., robotic arms learning to grasp objects).

# #### **Common Algorithms:**
# - Q-Learning
# - Deep Q-Networks (DQN)
# - Policy Gradients
# - Proximal Policy Optimization (PPO)

# ---

# ## **3. How Machine Learning Works (Step-by-Step)**
# ### **Step 1: Problem Definition**
# - Identify the **goal** (e.g., predict sales, classify images, recommend products).
# - Choose the **ML approach** (supervised, unsupervised, reinforcement).

# ### **Step 2: Data Collection & Preprocessing**
# - **Data Sources:** Databases, APIs, web scraping, sensors.
# - **Cleaning:** Handle missing values, remove duplicates.
# - **Transformation:** Normalization, encoding (e.g., one-hot encoding for categorical data).
# - **Feature Engineering:** Select relevant features (e.g., extracting text features for NLP).

# ### **Step 3: Model Selection**
# - **Supervised:** Choose between regression, classification, etc.
# - **Unsupervised:** Pick clustering or dimensionality reduction.
# - **Reinforcement:** Select an RL algorithm.

# ### **Step 4: Training the Model**
# - Split data into **training (70-80%)** and **testing (20-30%)** sets.
# - Feed training data into the model.
# - The model **adjusts its parameters** (e.g., weights in neural networks) to minimize error (loss function).

# ### **Step 5: Evaluation & Optimization**
# - **Metrics:**
#   - **Classification:** Accuracy, Precision, Recall, F1-Score, ROC-AUC.
#   - **Regression:** Mean Squared Error (MSE), R² Score.
#   - **Clustering:** Silhouette Score, Davies-Bouldin Index.
# - **Hyperparameter Tuning:** Adjust learning rate, number of layers, etc. (using GridSearchCV, RandomSearch).
# - **Cross-Validation:** Ensures model generalizes well (e.g., k-fold validation).

# ### **Step 6: Deployment & Monitoring**
# - **Deployment:** Deploy the model in production (e.g., Flask API, cloud services like AWS SageMaker).
# - **Monitoring:** Track performance over time, retrain if data drift occurs.

# ---

# ## **4. Key Machine Learning Algorithms**
# | **Type**          | **Algorithm**               | **Use Case** |
# |-------------------|----------------------------|-------------|
# | **Supervised**    | Linear Regression          | Predicting continuous values (e.g., house prices) |
# |                   | Logistic Regression        | Binary classification (e.g., spam detection) |
# |                   | Decision Trees            | Rule-based decisions (e.g., loan approval) |
# |                   | Random Forest             | Ensemble method for classification/regression |
# |                   | SVM (Support Vector Machine) | High-dimensional data (e.g., text classification) |
# |                   | Neural Networks           | Image recognition, NLP, deep learning |
# | **Unsupervised**  | K-Means Clustering        | Customer segmentation |
# |                   | PCA (Principal Component Analysis) | Dimensionality reduction |
# | **Reinforcement** | Q-Learning                | Game AI (e.g., Atari games) |
# |                   | Deep Q-Networks (DQN)     | Autonomous driving |

# ---

# ## **5. Applications of Machine Learning**
# | **Industry**       | **Applications** |
# |--------------------|----------------|
# | **Healthcare**     | Disease prediction, drug discovery, medical imaging (X-rays, MRIs) |
# | **Finance**        | Fraud detection, credit scoring, algorithmic trading |
# | **Retail**         | Recommendation systems (Amazon, Netflix), demand forecasting |
# | **Automotive**     | Self-driving cars (Tesla, Waymo), predictive maintenance |
# | **Entertainment**  | Voice assistants (Siri, Alexa), personalized ads |
# | **Manufacturing**  | Quality control, supply chain optimization |
# | **Cybersecurity**  | Anomaly detection, malware identification |

# ---

# ## **6. Challenges in Machine Learning**
# 1. **Data Quality Issues:**
#    - Missing values, noise, bias in data.
# 2. **Overfitting vs. Underfitting:**
#    - **Overfitting:** Model memorizes training data but fails on new data.
#    - **Underfitting:** Model is too simple to capture patterns.
# 3. **Computational Cost:**
#    - Deep learning models require high-end GPUs/TPUs.
# 4. **Interpretability:**
#    - Black-box models (e.g., neural networks) are hard to explain.
# 5. **Ethical Concerns:**
#    - Bias in training data (e.g., facial recognition disparities).
#    - Privacy issues (e.g., GDPR compliance).

# ---

# ## **7. Future of Machine Learning**
# - **Explainable AI (XAI):** Making models more interpretable.
# - **AutoML:** Automating model selection and hyperparameter tuning.
# - **Federated Learning:** Training models across decentralized devices (privacy-preserving).
# - **Quantum ML:** Leveraging quantum computing for faster training.
# - **Edge AI:** Running ML models on IoT devices (e.g., smartphones, drones).

# ---

# ## **8. Tools & Frameworks for Machine Learning**
# | **Category**       | **Tools & Libraries** |
# |--------------------|----------------------|
# | **Programming**    | Python, R, Julia |
# | **Data Processing** | Pandas, NumPy, Dask |
# | **Visualization**  | Matplotlib, Seaborn, Plotly |
# | **ML Libraries**   | Scikit-learn, TensorFlow, PyTorch, Keras |
# | **Big Data**       | Spark MLlib, H2O.ai |
# | **Deployment**     | Flask, FastAPI, Docker, AWS SageMaker |

# ---

# ## **9. Example: Building a Simple ML Model (Python)**
# Here’s a basic example of a **Supervised Learning** model using **Scikit-learn**:

# ```python
# # Step 1: Import libraries
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Step 2: Load dataset
# data = load_iris()
# X = data.data  # Features
# y = data.target  # Labels

# # Step 3: Split into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Step 4: Train the model
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# # Step 5: Make predictions
# predictions = model.predict(X_test)

# # Step 6: Evaluate
# accuracy = accuracy_score(y_test, predictions)
# print(f"Model Accuracy: {accuracy * 100:.2f}%")
# ```
# **Output:**
# ```
# Model Accuracy: 100.00%
# ```

# ---

# ## **10. Conclusion**
# Machine Learning is a **powerful tool** that enables computers to **learn from data** and make **data-driven decisions**. It has revolutionized industries by automating complex tasks, improving predictions, and uncovering hidden insights.

# ### **Key Takeaways:**
# ✅ **Three main types:** Supervised, Unsupervised, Reinforcement Learning.
# ✅ **Works by learning patterns from data** rather than explicit programming.
# ✅ **Requires high-quality data, proper preprocessing, and model evaluation.**
# ✅ **Applications span healthcare, finance, retail, automotive, and more.**
# ✅ **Challenges include overfitting, interpretability, and computational costs.**
# ✅ **Future trends include explainable AI, AutoML, and quantum ML.**

# Would you like a deeper dive into any specific aspect (e.g., neural networks, deep learning, or real-world case studies)? 🚀




#SUPPOSE IN PARALLEL EXECUTION WE HAVE TO SEND DIFFRENT PROMPT TO SHORT AND DIFFRENT TO DETAILED
#IN THAT CASE WE HAVE TO GIVE PROMPT TO SHORT AND DETAILED BU CREATING DICT. IN INVOKE FUNCTION

# result = chain.invoke({
#     "short": {"topic" : "Machine Learning"}, #we created dictonary here also as there can be multiple inputs
#     "detailed" : {"topic": "Deep Learning"}
# })

#it will give as it will go to runnableparallel , which is telling it wants topic but dict, is being given so will show error

#SO HERE WE HAVE TO USE ONE MORE RUNNABLE WHICH IS KNOWN AS RUNNABLE LAMBDA

#BY USING RunnableLambda we can use lambda exp. inside our pipeline



chain = RunnableParallel({
"short" :RunnableLambda(lambda x: x['short'])| short_prompt | model | parser,
"detailed" : RunnableLambda(lambda x: x['detailed']) |detailed_prompt | model | parser
})



result = chain.invoke({
     "short": {"topic" : "Machine Learning"}, #we created dictonary here also as there can be multiple inputs
     "detailed" : {"topic": "Deep Learning"}
 })



print(result['short'])
print(result['detailed'])


#OUTPUT >> 


# Machine Learning (ML) is a subset of Artificial Intelligence that enables systems to learn patterns from data and improve their performance over time without explicit programming. It uses algorithms to identify relationships and make predictions or decisions based on input data.
# ### **Deep Learning: A Comprehensive Explanation**

# Deep learning is a subset of **machine learning** that uses **artificial neural networks** with multiple layers (hence "deep") to model and solve complex problems. Inspired by the structure and function of the human brain, deep learning algorithms automatically learn hierarchical representations of data, enabling breakthroughs in fields like computer vision, natural language processing (NLP), speech recognition, and robotics.

# ---

# ## **1. Foundations of Deep Learning**
# ### **1.1 Neural Networks (Biological Inspiration)**
# Deep learning models are inspired by **biological neurons**, which process and transmit information via electrical and chemical signals. A **neuron** in a neural network:
# - Takes multiple **input signals** (like dendrites in a brain cell).
# - Applies a **weighted sum** (synaptic strength) to these inputs.
# - Passes the result through an **activation function** (like firing a neuron if threshold is exceeded).
# - Outputs a signal (axon).

# ### **1.2 Artificial Neural Networks (ANNs)**
# An ANN is a computational model consisting of:
# - **Input Layer** (receives raw data).
# - **Hidden Layers** (intermediate processing, can be multiple).
# - **Output Layer** (produces final prediction).

# Each layer applies **non-linear transformations**, allowing the network to learn complex patterns.

# ---

# ## **2. Key Concepts in Deep Learning**
# ### **2.1 Activation Functions**
# Activation functions introduce **non-linearity**, enabling neural networks to learn complex relationships. Common ones include:
# - **Sigmoid** (S-shaped, outputs between 0 and 1).
# - **Tanh** (S-shaped, outputs between -1 and 1).
# - **ReLU (Rectified Linear Unit)** (outputs max(0, x), most widely used).
# - **Leaky ReLU** (avoids dying ReLU problem).
# - **Softmax** (used in classification for probability distribution).

# ### **2.2 Loss Functions (Cost Functions)**
# Measure how well the model performs. Common loss functions:
# - **Mean Squared Error (MSE)** (for regression).
# - **Cross-Entropy Loss** (for classification).
# - **Hinge Loss** (used in SVMs).

# ### **2.3 Optimization Algorithms (Training)**
# Used to minimize the loss function by adjusting weights. Popular optimizers:
# - **Stochastic Gradient Descent (SGD)** (basic, slow convergence).
# - **Adam (Adaptive Moment Estimation)** (adapts learning rate, widely used).
# - **RMSprop** (adjusts learning rate per parameter).
# - **Adagrad** (adaptive learning rate for sparse data).

# ### **2.4 Backpropagation**
# A method to **update weights** by propagating the error backward through the network using the **chain rule of calculus**. Steps:
# 1. **Forward Pass**: Compute predictions.
# 2. **Compute Loss**: Compare predictions with true labels.
# 3. **Backward Pass**: Calculate gradients of loss w.r.t. weights.
# 4. **Update Weights**: Adjust weights using optimizer (e.g., SGD, Adam).

# ---

# ## **3. Types of Deep Learning Models**
# ### **3.1 Feedforward Neural Networks (FNNs / MLPs)**
# - **Simplest form** of deep learning.
# - Data flows in **one direction** (input → hidden layers → output).
# - Used for **tabular data, regression, classification**.

# ### **3.2 Convolutional Neural Networks (CNNs)**
# - **Specialized for grid-like data** (images, videos).
# - **Key Components**:
#   - **Convolutional Layers** (apply filters to detect features like edges, textures).
#   - **Pooling Layers** (reduce spatial dimensions, e.g., Max Pooling).
#   - **Fully Connected Layers** (for final classification).
# - **Applications**: Image recognition, object detection, medical imaging.

# ### **3.3 Recurrent Neural Networks (RNNs)**
# - **Designed for sequential data** (time series, text).
# - **Maintains a "memory"** via **hidden state**.
# - **Variants**:
#   - **LSTM (Long Short-Term Memory)** – Solves vanishing gradient problem.
#   - **GRU (Gated Recurrent Unit)** – Simplified LSTM.
# - **Applications**: Speech recognition, machine translation, stock prediction.

# ### **3.4 Transformers**
# - **Replaced RNNs/LSTMs** for sequential data (especially NLP).
# - **Key Features**:
#   - **Self-Attention Mechanism** (weighs importance of each word).
#   - **Parallel Processing** (unlike RNNs, which process sequentially).
# - **Applications**: BERT, GPT, Google’s T5.
# - **Architecture**:
#   - **Encoder** (processes input).
#   - **Decoder** (generates output).

# ### **3.5 Autoencoders**
# - **Unsupervised learning** for **dimensionality reduction & feature extraction**.
# - **Structure**:
#   - **Encoder** (compresses input into a latent space).
#   - **Decoder** (reconstructs input from latent space).
# - **Variants**:
#   - **Denoising Autoencoder** (reconstructs from corrupted input).
#   - **Variational Autoencoder (VAE)** (generative model).

# ### **3.6 Generative Adversarial Networks (GANs)**
# - **Two competing networks**:
#   - **Generator** (creates fake data).
#   - **Discriminator** (distinguishes real vs. fake data).
# - **Applications**: Image generation (e.g., Deepfakes), super-resolution.

# ### **3.7 Reinforcement Learning (RL) with Deep Learning**
# - **Agent learns by interacting with an environment** to maximize reward.
# - **Deep Q-Networks (DQN)** combine Q-learning with CNNs.
# - **Applications**: Robotics, game AI (AlphaGo), autonomous driving.

# ---

# ## **4. Training Deep Learning Models**
# ### **4.1 Data Preprocessing**
# - **Normalization** (scaling data to [0,1] or [-1,1]).
# - **Augmentation** (for images: rotation, flipping, cropping).
# - **Handling Missing Data** (imputation, masking).

# ### **4.2 Overfitting & Regularization**
# - **Overfitting**: Model memorizes training data but fails on test data.
# - **Solutions**:
#   - **Dropout** (randomly deactivates neurons during training).
#   - **L1/L2 Regularization** (penalizes large weights).
#   - **Early Stopping** (stops training when validation loss increases).
#   - **Batch Normalization** (normalizes layer inputs for stability).

# ### **4.3 Hyperparameter Tuning**
# - **Learning Rate** (too high → divergence; too low → slow training).
# - **Batch Size** (small batches → noisy updates; large batches → memory issues).
# - **Number of Layers & Neurons** (deeper networks learn complex patterns but risk overfitting).

# ### **4.4 Transfer Learning**
# - **Pre-trained models** (e.g., ResNet, BERT) are fine-tuned for new tasks.
# - **Benefits**: Saves training time, works well with small datasets.

# ---

# ## **5. Challenges in Deep Learning**
# | **Challenge** | **Description** | **Solutions** |
# |--------------|----------------|--------------|
# | **Vanishing/Exploding Gradients** | Gradients become too small/large, preventing learning. | ReLU, Batch Norm, Residual Connections (ResNet) |
# | **Overfitting** | Model performs well on training but poorly on test data. | Dropout, Regularization, Early Stopping |
# | **Computational Cost** | Training deep models requires high GPU/TPU power. | Distributed Training, Model Pruning |
# | **Interpretability** | Black-box nature makes it hard to explain decisions. | SHAP, LIME, Attention Mechanisms |
# | **Data Hunger** | Deep learning needs massive labeled datasets. | Data Augmentation, Synthetic Data (GANs) |
# | **Bias & Fairness** | Models may inherit biases from training data. | Fairness-aware algorithms, Diverse Datasets |

# ---

# ## **6. Applications of Deep Learning**
# | **Domain** | **Applications** | **Example Models** |
# |------------|----------------|-------------------|
# | **Computer Vision** | Image Classification, Object Detection, Segmentation | ResNet, YOLO, U-Net |
# | **Natural Language Processing (NLP)** | Machine Translation, Sentiment Analysis, Chatbots | BERT, Transformer, GPT-3 |
# | **Speech & Audio** | Speech Recognition, Voice Assistants | DeepSpeech, WaveNet |
# | **Healthcare** | Disease Diagnosis, Drug Discovery, Medical Imaging | CNN, RNN, GANs |
# | **Autonomous Vehicles** | Self-Driving Cars, Lane Detection | CNN + LSTM |
# | **Recommendation Systems** | Personalized Recommendations (Netflix, Amazon) | Collaborative Filtering + Deep Learning |
# | **Finance** | Fraud Detection, Algorithmic Trading | LSTM, Reinforcement Learning |
# | **Robotics** | Motion Planning, Grasping Objects | Deep Q-Networks (DQN) |

# ---

# ## **7. Future of Deep Learning**
# - **Explainable AI (XAI)**: Making models more interpretable.
# - **Neural Architecture Search (NAS)**: Automating model design.
# - **Few-Shot Learning**: Learning from small datasets.
# - **Edge AI**: Running models on mobile/embedded devices.
# - **Hybrid Models**: Combining deep learning with symbolic AI.
# - **Brain-Inspired Computing**: Mimicking biological neural networks (e.g., Spiking Neural Networks).

# ---

# ## **8. Tools & Frameworks**
# | **Tool** | **Description** |
# |----------|----------------|
# | **TensorFlow** (Google) | Open-source library for deep learning (supports CNNs, RNNs) |
# | **PyTorch** (Facebook) | Flexible, Python-first framework (used in research) |
# | **Keras** | High-level API (runs on TensorFlow) |
# | **OpenCV** | Computer vision library |
# | **Hugging Face Transformers** | NLP models (BERT, GPT) |
# | **FastAI** | High-level deep learning library |
# | **ONNX** | Open standard for model interoperability |

# ---

# ## **9. Conclusion**
# Deep learning has revolutionized AI by enabling machines to **automatically learn hierarchical features** from raw data. While it excels in complex tasks (e.g., image recognition, NLP), challenges like **computational cost, interpretability, and data requirements** persist. As research advances, deep learning will continue to push boundaries in **autonomy, creativity, and decision-making**.

# Would you like a deeper dive into any specific aspect (e.g., CNNs, Transformers, GANs)?
