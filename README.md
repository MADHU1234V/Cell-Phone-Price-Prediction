# 📱 Cell Phone Price Prediction

## What is this project?
This project predicts the price range of a mobile phone.
You just enter some details about the phone and it tells 
you whether the phone is Low Cost, Medium Cost, 
High Cost or Very High Cost.

---

## Why I made this project?
Mobile phone prices vary a lot in the market.
This project uses Machine Learning to automatically 
predict the price range based on phone specifications 
like RAM, Battery, Screen size etc.

---

## What can this project do?
- Enter phone details in a simple web form
- Click the Predict button
- Get the price range result instantly

---

## Price Range Meaning
| Number | Meaning |
|--------|---------|
| 0 | Low Cost |
| 1 | Medium Cost |
| 2 | High Cost |
| 3 | Very High Cost |

---

## What details do you enter?
| Input | Example |
|-------|---------|
| RAM | 3000 MB |
| Battery Power | 1500 mAh |
| Pixel Height | 1000 |
| Pixel Width | 1500 |
| 3G Support | Yes or No |
| 4G Support | Yes or No |

---

## Tools and Technologies Used
| What | Why |
|------|-----|
| Python | Programming language |
| Pandas | To read and clean the data |
| NumPy | For calculations |
| Matplotlib & Seaborn | To make graphs and charts |
| Scikit-learn | To build the ML model |
| Flask | To build the website |
| HTML & CSS | For the web page design |
| Pickle | To save the trained model |
| Jupyter Notebook | To write and run the code |

---

## Machine Learning Models I Tried
| Model | Result |
|-------|--------|
| Logistic Regression | Best|
| Decision Tree | Good |
| Support Vector Machine | Good |
| K-Nearest Neighbors | Good |
| Random Forest | Good|

> I used Random Forest because it gave the best accuracy

---

## Files in this Project
| File Name | What it does |
|-----------|-------------|
| cell.py | Main Flask app that runs the website |
| index.html | The web page where you enter phone details |
| style.css | Makes the web page look good |
| Cellphoneprice.csv | The dataset with 2000 phone records |
| Cell_phone_price-3.ipynb | Notebook where I built the ML model |
| CellPricePrediction.pkl | The saved trained model |
| CellPricePrediction1.pkl | The saved feature names |
