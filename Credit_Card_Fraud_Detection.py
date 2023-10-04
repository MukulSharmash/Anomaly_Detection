{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TDnoEQTWStTz"
      },
      "source": [
        "Importing the Dependencies"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hlNfrSC1PGfZ"
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "W0CTsNioTKnJ"
      },
      "source": [
        "# loading the dataset to a Pandas DataFrame\n",
        "credit_card_data = pd.read_csv('/content/credit_data.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 218
        },
        "id": "o_iMfyHsTa6s",
        "outputId": "318bdb4d-9f20-4789-c6e6-9b2de1aad091"
      },
      "source": [
        "# first 5 rows of the dataset\n",
        "credit_card_data.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "      <th>Class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.0</td>\n",
              "      <td>-1.359807</td>\n",
              "      <td>-0.072781</td>\n",
              "      <td>2.536347</td>\n",
              "      <td>1.378155</td>\n",
              "      <td>-0.338321</td>\n",
              "      <td>0.462388</td>\n",
              "      <td>0.239599</td>\n",
              "      <td>0.098698</td>\n",
              "      <td>0.363787</td>\n",
              "      <td>0.090794</td>\n",
              "      <td>-0.551600</td>\n",
              "      <td>-0.617801</td>\n",
              "      <td>-0.991390</td>\n",
              "      <td>-0.311169</td>\n",
              "      <td>1.468177</td>\n",
              "      <td>-0.470401</td>\n",
              "      <td>0.207971</td>\n",
              "      <td>0.025791</td>\n",
              "      <td>0.403993</td>\n",
              "      <td>0.251412</td>\n",
              "      <td>-0.018307</td>\n",
              "      <td>0.277838</td>\n",
              "      <td>-0.110474</td>\n",
              "      <td>0.066928</td>\n",
              "      <td>0.128539</td>\n",
              "      <td>-0.189115</td>\n",
              "      <td>0.133558</td>\n",
              "      <td>-0.021053</td>\n",
              "      <td>149.62</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0.0</td>\n",
              "      <td>1.191857</td>\n",
              "      <td>0.266151</td>\n",
              "      <td>0.166480</td>\n",
              "      <td>0.448154</td>\n",
              "      <td>0.060018</td>\n",
              "      <td>-0.082361</td>\n",
              "      <td>-0.078803</td>\n",
              "      <td>0.085102</td>\n",
              "      <td>-0.255425</td>\n",
              "      <td>-0.166974</td>\n",
              "      <td>1.612727</td>\n",
              "      <td>1.065235</td>\n",
              "      <td>0.489095</td>\n",
              "      <td>-0.143772</td>\n",
              "      <td>0.635558</td>\n",
              "      <td>0.463917</td>\n",
              "      <td>-0.114805</td>\n",
              "      <td>-0.183361</td>\n",
              "      <td>-0.145783</td>\n",
              "      <td>-0.069083</td>\n",
              "      <td>-0.225775</td>\n",
              "      <td>-0.638672</td>\n",
              "      <td>0.101288</td>\n",
              "      <td>-0.339846</td>\n",
              "      <td>0.167170</td>\n",
              "      <td>0.125895</td>\n",
              "      <td>-0.008983</td>\n",
              "      <td>0.014724</td>\n",
              "      <td>2.69</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1.0</td>\n",
              "      <td>-1.358354</td>\n",
              "      <td>-1.340163</td>\n",
              "      <td>1.773209</td>\n",
              "      <td>0.379780</td>\n",
              "      <td>-0.503198</td>\n",
              "      <td>1.800499</td>\n",
              "      <td>0.791461</td>\n",
              "      <td>0.247676</td>\n",
              "      <td>-1.514654</td>\n",
              "      <td>0.207643</td>\n",
              "      <td>0.624501</td>\n",
              "      <td>0.066084</td>\n",
              "      <td>0.717293</td>\n",
              "      <td>-0.165946</td>\n",
              "      <td>2.345865</td>\n",
              "      <td>-2.890083</td>\n",
              "      <td>1.109969</td>\n",
              "      <td>-0.121359</td>\n",
              "      <td>-2.261857</td>\n",
              "      <td>0.524980</td>\n",
              "      <td>0.247998</td>\n",
              "      <td>0.771679</td>\n",
              "      <td>0.909412</td>\n",
              "      <td>-0.689281</td>\n",
              "      <td>-0.327642</td>\n",
              "      <td>-0.139097</td>\n",
              "      <td>-0.055353</td>\n",
              "      <td>-0.059752</td>\n",
              "      <td>378.66</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.0</td>\n",
              "      <td>-0.966272</td>\n",
              "      <td>-0.185226</td>\n",
              "      <td>1.792993</td>\n",
              "      <td>-0.863291</td>\n",
              "      <td>-0.010309</td>\n",
              "      <td>1.247203</td>\n",
              "      <td>0.237609</td>\n",
              "      <td>0.377436</td>\n",
              "      <td>-1.387024</td>\n",
              "      <td>-0.054952</td>\n",
              "      <td>-0.226487</td>\n",
              "      <td>0.178228</td>\n",
              "      <td>0.507757</td>\n",
              "      <td>-0.287924</td>\n",
              "      <td>-0.631418</td>\n",
              "      <td>-1.059647</td>\n",
              "      <td>-0.684093</td>\n",
              "      <td>1.965775</td>\n",
              "      <td>-1.232622</td>\n",
              "      <td>-0.208038</td>\n",
              "      <td>-0.108300</td>\n",
              "      <td>0.005274</td>\n",
              "      <td>-0.190321</td>\n",
              "      <td>-1.175575</td>\n",
              "      <td>0.647376</td>\n",
              "      <td>-0.221929</td>\n",
              "      <td>0.062723</td>\n",
              "      <td>0.061458</td>\n",
              "      <td>123.50</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2.0</td>\n",
              "      <td>-1.158233</td>\n",
              "      <td>0.877737</td>\n",
              "      <td>1.548718</td>\n",
              "      <td>0.403034</td>\n",
              "      <td>-0.407193</td>\n",
              "      <td>0.095921</td>\n",
              "      <td>0.592941</td>\n",
              "      <td>-0.270533</td>\n",
              "      <td>0.817739</td>\n",
              "      <td>0.753074</td>\n",
              "      <td>-0.822843</td>\n",
              "      <td>0.538196</td>\n",
              "      <td>1.345852</td>\n",
              "      <td>-1.119670</td>\n",
              "      <td>0.175121</td>\n",
              "      <td>-0.451449</td>\n",
              "      <td>-0.237033</td>\n",
              "      <td>-0.038195</td>\n",
              "      <td>0.803487</td>\n",
              "      <td>0.408542</td>\n",
              "      <td>-0.009431</td>\n",
              "      <td>0.798278</td>\n",
              "      <td>-0.137458</td>\n",
              "      <td>0.141267</td>\n",
              "      <td>-0.206010</td>\n",
              "      <td>0.502292</td>\n",
              "      <td>0.219422</td>\n",
              "      <td>0.215153</td>\n",
              "      <td>69.99</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   Time        V1        V2        V3  ...       V27       V28  Amount  Class\n",
              "0   0.0 -1.359807 -0.072781  2.536347  ...  0.133558 -0.021053  149.62      0\n",
              "1   0.0  1.191857  0.266151  0.166480  ... -0.008983  0.014724    2.69      0\n",
              "2   1.0 -1.358354 -1.340163  1.773209  ... -0.055353 -0.059752  378.66      0\n",
              "3   1.0 -0.966272 -0.185226  1.792993  ...  0.062723  0.061458  123.50      0\n",
              "4   2.0 -1.158233  0.877737  1.548718  ...  0.219422  0.215153   69.99      0\n",
              "\n",
              "[5 rows x 31 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 218
        },
        "id": "iWCP6YJjThIM",
        "outputId": "19097c05-c0ff-4df7-c21b-84c7cde9e7da"
      },
      "source": [
        "credit_card_data.tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "      <th>Class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>284802</th>\n",
              "      <td>172786.0</td>\n",
              "      <td>-11.881118</td>\n",
              "      <td>10.071785</td>\n",
              "      <td>-9.834783</td>\n",
              "      <td>-2.066656</td>\n",
              "      <td>-5.364473</td>\n",
              "      <td>-2.606837</td>\n",
              "      <td>-4.918215</td>\n",
              "      <td>7.305334</td>\n",
              "      <td>1.914428</td>\n",
              "      <td>4.356170</td>\n",
              "      <td>-1.593105</td>\n",
              "      <td>2.711941</td>\n",
              "      <td>-0.689256</td>\n",
              "      <td>4.626942</td>\n",
              "      <td>-0.924459</td>\n",
              "      <td>1.107641</td>\n",
              "      <td>1.991691</td>\n",
              "      <td>0.510632</td>\n",
              "      <td>-0.682920</td>\n",
              "      <td>1.475829</td>\n",
              "      <td>0.213454</td>\n",
              "      <td>0.111864</td>\n",
              "      <td>1.014480</td>\n",
              "      <td>-0.509348</td>\n",
              "      <td>1.436807</td>\n",
              "      <td>0.250034</td>\n",
              "      <td>0.943651</td>\n",
              "      <td>0.823731</td>\n",
              "      <td>0.77</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>284803</th>\n",
              "      <td>172787.0</td>\n",
              "      <td>-0.732789</td>\n",
              "      <td>-0.055080</td>\n",
              "      <td>2.035030</td>\n",
              "      <td>-0.738589</td>\n",
              "      <td>0.868229</td>\n",
              "      <td>1.058415</td>\n",
              "      <td>0.024330</td>\n",
              "      <td>0.294869</td>\n",
              "      <td>0.584800</td>\n",
              "      <td>-0.975926</td>\n",
              "      <td>-0.150189</td>\n",
              "      <td>0.915802</td>\n",
              "      <td>1.214756</td>\n",
              "      <td>-0.675143</td>\n",
              "      <td>1.164931</td>\n",
              "      <td>-0.711757</td>\n",
              "      <td>-0.025693</td>\n",
              "      <td>-1.221179</td>\n",
              "      <td>-1.545556</td>\n",
              "      <td>0.059616</td>\n",
              "      <td>0.214205</td>\n",
              "      <td>0.924384</td>\n",
              "      <td>0.012463</td>\n",
              "      <td>-1.016226</td>\n",
              "      <td>-0.606624</td>\n",
              "      <td>-0.395255</td>\n",
              "      <td>0.068472</td>\n",
              "      <td>-0.053527</td>\n",
              "      <td>24.79</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>284804</th>\n",
              "      <td>172788.0</td>\n",
              "      <td>1.919565</td>\n",
              "      <td>-0.301254</td>\n",
              "      <td>-3.249640</td>\n",
              "      <td>-0.557828</td>\n",
              "      <td>2.630515</td>\n",
              "      <td>3.031260</td>\n",
              "      <td>-0.296827</td>\n",
              "      <td>0.708417</td>\n",
              "      <td>0.432454</td>\n",
              "      <td>-0.484782</td>\n",
              "      <td>0.411614</td>\n",
              "      <td>0.063119</td>\n",
              "      <td>-0.183699</td>\n",
              "      <td>-0.510602</td>\n",
              "      <td>1.329284</td>\n",
              "      <td>0.140716</td>\n",
              "      <td>0.313502</td>\n",
              "      <td>0.395652</td>\n",
              "      <td>-0.577252</td>\n",
              "      <td>0.001396</td>\n",
              "      <td>0.232045</td>\n",
              "      <td>0.578229</td>\n",
              "      <td>-0.037501</td>\n",
              "      <td>0.640134</td>\n",
              "      <td>0.265745</td>\n",
              "      <td>-0.087371</td>\n",
              "      <td>0.004455</td>\n",
              "      <td>-0.026561</td>\n",
              "      <td>67.88</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>284805</th>\n",
              "      <td>172788.0</td>\n",
              "      <td>-0.240440</td>\n",
              "      <td>0.530483</td>\n",
              "      <td>0.702510</td>\n",
              "      <td>0.689799</td>\n",
              "      <td>-0.377961</td>\n",
              "      <td>0.623708</td>\n",
              "      <td>-0.686180</td>\n",
              "      <td>0.679145</td>\n",
              "      <td>0.392087</td>\n",
              "      <td>-0.399126</td>\n",
              "      <td>-1.933849</td>\n",
              "      <td>-0.962886</td>\n",
              "      <td>-1.042082</td>\n",
              "      <td>0.449624</td>\n",
              "      <td>1.962563</td>\n",
              "      <td>-0.608577</td>\n",
              "      <td>0.509928</td>\n",
              "      <td>1.113981</td>\n",
              "      <td>2.897849</td>\n",
              "      <td>0.127434</td>\n",
              "      <td>0.265245</td>\n",
              "      <td>0.800049</td>\n",
              "      <td>-0.163298</td>\n",
              "      <td>0.123205</td>\n",
              "      <td>-0.569159</td>\n",
              "      <td>0.546668</td>\n",
              "      <td>0.108821</td>\n",
              "      <td>0.104533</td>\n",
              "      <td>10.00</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>284806</th>\n",
              "      <td>172792.0</td>\n",
              "      <td>-0.533413</td>\n",
              "      <td>-0.189733</td>\n",
              "      <td>0.703337</td>\n",
              "      <td>-0.506271</td>\n",
              "      <td>-0.012546</td>\n",
              "      <td>-0.649617</td>\n",
              "      <td>1.577006</td>\n",
              "      <td>-0.414650</td>\n",
              "      <td>0.486180</td>\n",
              "      <td>-0.915427</td>\n",
              "      <td>-1.040458</td>\n",
              "      <td>-0.031513</td>\n",
              "      <td>-0.188093</td>\n",
              "      <td>-0.084316</td>\n",
              "      <td>0.041333</td>\n",
              "      <td>-0.302620</td>\n",
              "      <td>-0.660377</td>\n",
              "      <td>0.167430</td>\n",
              "      <td>-0.256117</td>\n",
              "      <td>0.382948</td>\n",
              "      <td>0.261057</td>\n",
              "      <td>0.643078</td>\n",
              "      <td>0.376777</td>\n",
              "      <td>0.008797</td>\n",
              "      <td>-0.473649</td>\n",
              "      <td>-0.818267</td>\n",
              "      <td>-0.002415</td>\n",
              "      <td>0.013649</td>\n",
              "      <td>217.00</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Time         V1         V2  ...       V28  Amount  Class\n",
              "284802  172786.0 -11.881118  10.071785  ...  0.823731    0.77      0\n",
              "284803  172787.0  -0.732789  -0.055080  ... -0.053527   24.79      0\n",
              "284804  172788.0   1.919565  -0.301254  ... -0.026561   67.88      0\n",
              "284805  172788.0  -0.240440   0.530483  ...  0.104533   10.00      0\n",
              "284806  172792.0  -0.533413  -0.189733  ...  0.013649  217.00      0\n",
              "\n",
              "[5 rows x 31 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KcCZquvEUD3A",
        "outputId": "a18d75ef-936b-4a52-8589-0acb2cc5fe4e"
      },
      "source": [
        "# dataset informations\n",
        "credit_card_data.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 284807 entries, 0 to 284806\n",
            "Data columns (total 31 columns):\n",
            " #   Column  Non-Null Count   Dtype  \n",
            "---  ------  --------------   -----  \n",
            " 0   Time    284807 non-null  float64\n",
            " 1   V1      284807 non-null  float64\n",
            " 2   V2      284807 non-null  float64\n",
            " 3   V3      284807 non-null  float64\n",
            " 4   V4      284807 non-null  float64\n",
            " 5   V5      284807 non-null  float64\n",
            " 6   V6      284807 non-null  float64\n",
            " 7   V7      284807 non-null  float64\n",
            " 8   V8      284807 non-null  float64\n",
            " 9   V9      284807 non-null  float64\n",
            " 10  V10     284807 non-null  float64\n",
            " 11  V11     284807 non-null  float64\n",
            " 12  V12     284807 non-null  float64\n",
            " 13  V13     284807 non-null  float64\n",
            " 14  V14     284807 non-null  float64\n",
            " 15  V15     284807 non-null  float64\n",
            " 16  V16     284807 non-null  float64\n",
            " 17  V17     284807 non-null  float64\n",
            " 18  V18     284807 non-null  float64\n",
            " 19  V19     284807 non-null  float64\n",
            " 20  V20     284807 non-null  float64\n",
            " 21  V21     284807 non-null  float64\n",
            " 22  V22     284807 non-null  float64\n",
            " 23  V23     284807 non-null  float64\n",
            " 24  V24     284807 non-null  float64\n",
            " 25  V25     284807 non-null  float64\n",
            " 26  V26     284807 non-null  float64\n",
            " 27  V27     284807 non-null  float64\n",
            " 28  V28     284807 non-null  float64\n",
            " 29  Amount  284807 non-null  float64\n",
            " 30  Class   284807 non-null  int64  \n",
            "dtypes: float64(30), int64(1)\n",
            "memory usage: 67.4 MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XxwasmfKUQiA",
        "outputId": "a1cf3e15-9491-40f9-fecb-e5d1895bc8ca"
      },
      "source": [
        "# checking the number of missing values in each column\n",
        "credit_card_data.isnull().sum()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Time      0\n",
              "V1        0\n",
              "V2        0\n",
              "V3        0\n",
              "V4        0\n",
              "V5        0\n",
              "V6        0\n",
              "V7        0\n",
              "V8        0\n",
              "V9        0\n",
              "V10       0\n",
              "V11       0\n",
              "V12       0\n",
              "V13       0\n",
              "V14       0\n",
              "V15       0\n",
              "V16       0\n",
              "V17       0\n",
              "V18       0\n",
              "V19       0\n",
              "V20       0\n",
              "V21       0\n",
              "V22       0\n",
              "V23       0\n",
              "V24       0\n",
              "V25       0\n",
              "V26       0\n",
              "V27       0\n",
              "V28       0\n",
              "Amount    0\n",
              "Class     0\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EIpoKfp5Ugri",
        "outputId": "5150aa81-723c-424d-dcee-80f5c1e37a0f"
      },
      "source": [
        "# distribution of legit transactions & fraudulent transactions\n",
        "credit_card_data['Class'].value_counts()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    284315\n",
              "1       492\n",
              "Name: Class, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "flz_InK7VGri"
      },
      "source": [
        "This Dataset is highly unblanced"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4OlMhkHzVKMv"
      },
      "source": [
        "0 --> Normal Transaction\n",
        "\n",
        "1 --> fraudulent transaction"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QNn77bdbU2Lf"
      },
      "source": [
        "# separating the data for analysis\n",
        "legit = credit_card_data[credit_card_data.Class == 0]\n",
        "fraud = credit_card_data[credit_card_data.Class == 1]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zsrMgOdoVnrV",
        "outputId": "3ca353f2-4339-435e-9e5b-b4080bf7f608"
      },
      "source": [
        "print(legit.shape)\n",
        "print(fraud.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(284315, 31)\n",
            "(492, 31)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1s3KGshBVsTb",
        "outputId": "a5a35c33-3ca5-47d0-d060-dc53c2497f71"
      },
      "source": [
        "# statistical measures of the data\n",
        "legit.Amount.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count    284315.000000\n",
              "mean         88.291022\n",
              "std         250.105092\n",
              "min           0.000000\n",
              "25%           5.650000\n",
              "50%          22.000000\n",
              "75%          77.050000\n",
              "max       25691.160000\n",
              "Name: Amount, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KkU3Mzr5V7fR",
        "outputId": "30e87d03-1587-45e9-bc27-fd7bc3a5a150"
      },
      "source": [
        "fraud.Amount.describe()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "count     492.000000\n",
              "mean      122.211321\n",
              "std       256.683288\n",
              "min         0.000000\n",
              "25%         1.000000\n",
              "50%         9.250000\n",
              "75%       105.890000\n",
              "max      2125.870000\n",
              "Name: Amount, dtype: float64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 158
        },
        "id": "aFUMMHwYWMvp",
        "outputId": "02e34b2d-07d0-4e64-9e79-a59bc22d7ed8"
      },
      "source": [
        "# compare the values for both transactions\n",
        "credit_card_data.groupby('Class').mean()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Class</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>94838.202258</td>\n",
              "      <td>0.008258</td>\n",
              "      <td>-0.006271</td>\n",
              "      <td>0.012171</td>\n",
              "      <td>-0.007860</td>\n",
              "      <td>0.005453</td>\n",
              "      <td>0.002419</td>\n",
              "      <td>0.009637</td>\n",
              "      <td>-0.000987</td>\n",
              "      <td>0.004467</td>\n",
              "      <td>0.009824</td>\n",
              "      <td>-0.006576</td>\n",
              "      <td>0.010832</td>\n",
              "      <td>0.000189</td>\n",
              "      <td>0.012064</td>\n",
              "      <td>0.000161</td>\n",
              "      <td>0.007164</td>\n",
              "      <td>0.011535</td>\n",
              "      <td>0.003887</td>\n",
              "      <td>-0.001178</td>\n",
              "      <td>-0.000644</td>\n",
              "      <td>-0.001235</td>\n",
              "      <td>-0.000024</td>\n",
              "      <td>0.000070</td>\n",
              "      <td>0.000182</td>\n",
              "      <td>-0.000072</td>\n",
              "      <td>-0.000089</td>\n",
              "      <td>-0.000295</td>\n",
              "      <td>-0.000131</td>\n",
              "      <td>88.291022</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>80746.806911</td>\n",
              "      <td>-4.771948</td>\n",
              "      <td>3.623778</td>\n",
              "      <td>-7.033281</td>\n",
              "      <td>4.542029</td>\n",
              "      <td>-3.151225</td>\n",
              "      <td>-1.397737</td>\n",
              "      <td>-5.568731</td>\n",
              "      <td>0.570636</td>\n",
              "      <td>-2.581123</td>\n",
              "      <td>-5.676883</td>\n",
              "      <td>3.800173</td>\n",
              "      <td>-6.259393</td>\n",
              "      <td>-0.109334</td>\n",
              "      <td>-6.971723</td>\n",
              "      <td>-0.092929</td>\n",
              "      <td>-4.139946</td>\n",
              "      <td>-6.665836</td>\n",
              "      <td>-2.246308</td>\n",
              "      <td>0.680659</td>\n",
              "      <td>0.372319</td>\n",
              "      <td>0.713588</td>\n",
              "      <td>0.014049</td>\n",
              "      <td>-0.040308</td>\n",
              "      <td>-0.105130</td>\n",
              "      <td>0.041449</td>\n",
              "      <td>0.051648</td>\n",
              "      <td>0.170575</td>\n",
              "      <td>0.075667</td>\n",
              "      <td>122.211321</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "               Time        V1        V2  ...       V27       V28      Amount\n",
              "Class                                    ...                                \n",
              "0      94838.202258  0.008258 -0.006271  ... -0.000295 -0.000131   88.291022\n",
              "1      80746.806911 -4.771948  3.623778  ...  0.170575  0.075667  122.211321\n",
              "\n",
              "[2 rows x 30 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ybHNYPpEW0N6"
      },
      "source": [
        "Under-Sampling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MlXkIGEIW3KM"
      },
      "source": [
        "Build a sample dataset containing similar distribution of normal transactions and Fraudulent Transactions"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "bCj3Dee7XB0F"
      },
      "source": [
        "Number of Fraudulent Transactions --> 492"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "QtWT13mKWjJ_"
      },
      "source": [
        "legit_sample = legit.sample(n=492)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SNiYI_SmXeim"
      },
      "source": [
        "Concatenating two DataFrames"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0yiXrYiRXcnE"
      },
      "source": [
        "new_dataset = pd.concat([legit_sample, fraud], axis=0)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 218
        },
        "id": "UuLw43AXX0bq",
        "outputId": "01db7f18-69a0-4579-b5c8-e51ca4f61096"
      },
      "source": [
        "new_dataset.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "      <th>Class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>203131</th>\n",
              "      <td>134666.0</td>\n",
              "      <td>-1.220220</td>\n",
              "      <td>-1.729458</td>\n",
              "      <td>-1.118957</td>\n",
              "      <td>-0.266099</td>\n",
              "      <td>0.823338</td>\n",
              "      <td>-0.098556</td>\n",
              "      <td>-0.407751</td>\n",
              "      <td>0.563010</td>\n",
              "      <td>-1.007790</td>\n",
              "      <td>0.261245</td>\n",
              "      <td>-0.841608</td>\n",
              "      <td>-0.041129</td>\n",
              "      <td>-0.628463</td>\n",
              "      <td>0.742288</td>\n",
              "      <td>-1.038836</td>\n",
              "      <td>-2.133763</td>\n",
              "      <td>0.200161</td>\n",
              "      <td>2.264390</td>\n",
              "      <td>0.791250</td>\n",
              "      <td>0.140809</td>\n",
              "      <td>0.237283</td>\n",
              "      <td>0.487028</td>\n",
              "      <td>0.286055</td>\n",
              "      <td>-0.119733</td>\n",
              "      <td>-0.909162</td>\n",
              "      <td>-0.117020</td>\n",
              "      <td>0.173995</td>\n",
              "      <td>-0.023852</td>\n",
              "      <td>155.00</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>95383</th>\n",
              "      <td>65279.0</td>\n",
              "      <td>-1.295124</td>\n",
              "      <td>0.157326</td>\n",
              "      <td>1.544771</td>\n",
              "      <td>-2.468209</td>\n",
              "      <td>-1.683113</td>\n",
              "      <td>-0.623764</td>\n",
              "      <td>-0.371798</td>\n",
              "      <td>0.505656</td>\n",
              "      <td>-2.243475</td>\n",
              "      <td>0.856381</td>\n",
              "      <td>-0.402158</td>\n",
              "      <td>-1.396842</td>\n",
              "      <td>-0.756093</td>\n",
              "      <td>0.014161</td>\n",
              "      <td>0.424519</td>\n",
              "      <td>-0.335512</td>\n",
              "      <td>0.863702</td>\n",
              "      <td>-0.542891</td>\n",
              "      <td>-1.189703</td>\n",
              "      <td>-0.277333</td>\n",
              "      <td>-0.415322</td>\n",
              "      <td>-0.894639</td>\n",
              "      <td>0.126543</td>\n",
              "      <td>0.296285</td>\n",
              "      <td>0.132186</td>\n",
              "      <td>-0.524334</td>\n",
              "      <td>0.317321</td>\n",
              "      <td>0.105345</td>\n",
              "      <td>70.00</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99706</th>\n",
              "      <td>67246.0</td>\n",
              "      <td>-1.481168</td>\n",
              "      <td>1.226490</td>\n",
              "      <td>1.857550</td>\n",
              "      <td>2.980777</td>\n",
              "      <td>-0.672645</td>\n",
              "      <td>0.581449</td>\n",
              "      <td>-0.143172</td>\n",
              "      <td>0.302713</td>\n",
              "      <td>-0.624670</td>\n",
              "      <td>1.452271</td>\n",
              "      <td>0.940775</td>\n",
              "      <td>0.778863</td>\n",
              "      <td>0.423377</td>\n",
              "      <td>-0.291527</td>\n",
              "      <td>-0.439764</td>\n",
              "      <td>-0.173737</td>\n",
              "      <td>0.072368</td>\n",
              "      <td>0.575807</td>\n",
              "      <td>1.107665</td>\n",
              "      <td>0.075344</td>\n",
              "      <td>0.255337</td>\n",
              "      <td>0.948105</td>\n",
              "      <td>-0.186967</td>\n",
              "      <td>0.590834</td>\n",
              "      <td>-0.499863</td>\n",
              "      <td>0.203458</td>\n",
              "      <td>-0.546577</td>\n",
              "      <td>0.076538</td>\n",
              "      <td>40.14</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>153895</th>\n",
              "      <td>100541.0</td>\n",
              "      <td>-0.181013</td>\n",
              "      <td>1.395877</td>\n",
              "      <td>1.204669</td>\n",
              "      <td>4.349279</td>\n",
              "      <td>1.330126</td>\n",
              "      <td>1.277520</td>\n",
              "      <td>1.568221</td>\n",
              "      <td>-0.633374</td>\n",
              "      <td>-0.860482</td>\n",
              "      <td>1.483849</td>\n",
              "      <td>-0.040592</td>\n",
              "      <td>-3.117997</td>\n",
              "      <td>2.814195</td>\n",
              "      <td>1.224039</td>\n",
              "      <td>0.074473</td>\n",
              "      <td>-0.316746</td>\n",
              "      <td>0.485181</td>\n",
              "      <td>-0.058099</td>\n",
              "      <td>1.263988</td>\n",
              "      <td>0.334418</td>\n",
              "      <td>-0.456328</td>\n",
              "      <td>-0.687657</td>\n",
              "      <td>-0.049974</td>\n",
              "      <td>0.191566</td>\n",
              "      <td>-0.558483</td>\n",
              "      <td>-0.029382</td>\n",
              "      <td>-0.229857</td>\n",
              "      <td>-0.329608</td>\n",
              "      <td>137.04</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>249976</th>\n",
              "      <td>154664.0</td>\n",
              "      <td>0.475977</td>\n",
              "      <td>-0.573662</td>\n",
              "      <td>0.480520</td>\n",
              "      <td>-2.524647</td>\n",
              "      <td>-0.616284</td>\n",
              "      <td>-0.361317</td>\n",
              "      <td>-0.347861</td>\n",
              "      <td>-0.108238</td>\n",
              "      <td>-1.876507</td>\n",
              "      <td>0.871271</td>\n",
              "      <td>-1.201188</td>\n",
              "      <td>-0.741241</td>\n",
              "      <td>1.189017</td>\n",
              "      <td>-0.811912</td>\n",
              "      <td>-0.605718</td>\n",
              "      <td>-0.435814</td>\n",
              "      <td>0.234379</td>\n",
              "      <td>0.052987</td>\n",
              "      <td>-0.362860</td>\n",
              "      <td>-0.310337</td>\n",
              "      <td>-0.092778</td>\n",
              "      <td>0.187082</td>\n",
              "      <td>0.062234</td>\n",
              "      <td>0.653392</td>\n",
              "      <td>-0.399247</td>\n",
              "      <td>-0.281990</td>\n",
              "      <td>0.058961</td>\n",
              "      <td>0.012816</td>\n",
              "      <td>19.60</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Time        V1        V2  ...       V28  Amount  Class\n",
              "203131  134666.0 -1.220220 -1.729458  ... -0.023852  155.00      0\n",
              "95383    65279.0 -1.295124  0.157326  ...  0.105345   70.00      0\n",
              "99706    67246.0 -1.481168  1.226490  ...  0.076538   40.14      0\n",
              "153895  100541.0 -0.181013  1.395877  ... -0.329608  137.04      0\n",
              "249976  154664.0  0.475977 -0.573662  ...  0.012816   19.60      0\n",
              "\n",
              "[5 rows x 31 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 218
        },
        "id": "n_Rjt1qDX3AQ",
        "outputId": "c2624d05-e2bf-41c5-e858-37f29314d18d"
      },
      "source": [
        "new_dataset.tail()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "      <th>Class</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>279863</th>\n",
              "      <td>169142.0</td>\n",
              "      <td>-1.927883</td>\n",
              "      <td>1.125653</td>\n",
              "      <td>-4.518331</td>\n",
              "      <td>1.749293</td>\n",
              "      <td>-1.566487</td>\n",
              "      <td>-2.010494</td>\n",
              "      <td>-0.882850</td>\n",
              "      <td>0.697211</td>\n",
              "      <td>-2.064945</td>\n",
              "      <td>-5.587794</td>\n",
              "      <td>2.115795</td>\n",
              "      <td>-5.417424</td>\n",
              "      <td>-1.235123</td>\n",
              "      <td>-6.665177</td>\n",
              "      <td>0.401701</td>\n",
              "      <td>-2.897825</td>\n",
              "      <td>-4.570529</td>\n",
              "      <td>-1.315147</td>\n",
              "      <td>0.391167</td>\n",
              "      <td>1.252967</td>\n",
              "      <td>0.778584</td>\n",
              "      <td>-0.319189</td>\n",
              "      <td>0.639419</td>\n",
              "      <td>-0.294885</td>\n",
              "      <td>0.537503</td>\n",
              "      <td>0.788395</td>\n",
              "      <td>0.292680</td>\n",
              "      <td>0.147968</td>\n",
              "      <td>390.00</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>280143</th>\n",
              "      <td>169347.0</td>\n",
              "      <td>1.378559</td>\n",
              "      <td>1.289381</td>\n",
              "      <td>-5.004247</td>\n",
              "      <td>1.411850</td>\n",
              "      <td>0.442581</td>\n",
              "      <td>-1.326536</td>\n",
              "      <td>-1.413170</td>\n",
              "      <td>0.248525</td>\n",
              "      <td>-1.127396</td>\n",
              "      <td>-3.232153</td>\n",
              "      <td>2.858466</td>\n",
              "      <td>-3.096915</td>\n",
              "      <td>-0.792532</td>\n",
              "      <td>-5.210141</td>\n",
              "      <td>-0.613803</td>\n",
              "      <td>-2.155297</td>\n",
              "      <td>-3.267116</td>\n",
              "      <td>-0.688505</td>\n",
              "      <td>0.737657</td>\n",
              "      <td>0.226138</td>\n",
              "      <td>0.370612</td>\n",
              "      <td>0.028234</td>\n",
              "      <td>-0.145640</td>\n",
              "      <td>-0.081049</td>\n",
              "      <td>0.521875</td>\n",
              "      <td>0.739467</td>\n",
              "      <td>0.389152</td>\n",
              "      <td>0.186637</td>\n",
              "      <td>0.76</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>280149</th>\n",
              "      <td>169351.0</td>\n",
              "      <td>-0.676143</td>\n",
              "      <td>1.126366</td>\n",
              "      <td>-2.213700</td>\n",
              "      <td>0.468308</td>\n",
              "      <td>-1.120541</td>\n",
              "      <td>-0.003346</td>\n",
              "      <td>-2.234739</td>\n",
              "      <td>1.210158</td>\n",
              "      <td>-0.652250</td>\n",
              "      <td>-3.463891</td>\n",
              "      <td>1.794969</td>\n",
              "      <td>-2.775022</td>\n",
              "      <td>-0.418950</td>\n",
              "      <td>-4.057162</td>\n",
              "      <td>-0.712616</td>\n",
              "      <td>-1.603015</td>\n",
              "      <td>-5.035326</td>\n",
              "      <td>-0.507000</td>\n",
              "      <td>0.266272</td>\n",
              "      <td>0.247968</td>\n",
              "      <td>0.751826</td>\n",
              "      <td>0.834108</td>\n",
              "      <td>0.190944</td>\n",
              "      <td>0.032070</td>\n",
              "      <td>-0.739695</td>\n",
              "      <td>0.471111</td>\n",
              "      <td>0.385107</td>\n",
              "      <td>0.194361</td>\n",
              "      <td>77.89</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>281144</th>\n",
              "      <td>169966.0</td>\n",
              "      <td>-3.113832</td>\n",
              "      <td>0.585864</td>\n",
              "      <td>-5.399730</td>\n",
              "      <td>1.817092</td>\n",
              "      <td>-0.840618</td>\n",
              "      <td>-2.943548</td>\n",
              "      <td>-2.208002</td>\n",
              "      <td>1.058733</td>\n",
              "      <td>-1.632333</td>\n",
              "      <td>-5.245984</td>\n",
              "      <td>1.933520</td>\n",
              "      <td>-5.030465</td>\n",
              "      <td>-1.127455</td>\n",
              "      <td>-6.416628</td>\n",
              "      <td>0.141237</td>\n",
              "      <td>-2.549498</td>\n",
              "      <td>-4.614717</td>\n",
              "      <td>-1.478138</td>\n",
              "      <td>-0.035480</td>\n",
              "      <td>0.306271</td>\n",
              "      <td>0.583276</td>\n",
              "      <td>-0.269209</td>\n",
              "      <td>-0.456108</td>\n",
              "      <td>-0.183659</td>\n",
              "      <td>-0.328168</td>\n",
              "      <td>0.606116</td>\n",
              "      <td>0.884876</td>\n",
              "      <td>-0.253700</td>\n",
              "      <td>245.00</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>281674</th>\n",
              "      <td>170348.0</td>\n",
              "      <td>1.991976</td>\n",
              "      <td>0.158476</td>\n",
              "      <td>-2.583441</td>\n",
              "      <td>0.408670</td>\n",
              "      <td>1.151147</td>\n",
              "      <td>-0.096695</td>\n",
              "      <td>0.223050</td>\n",
              "      <td>-0.068384</td>\n",
              "      <td>0.577829</td>\n",
              "      <td>-0.888722</td>\n",
              "      <td>0.491140</td>\n",
              "      <td>0.728903</td>\n",
              "      <td>0.380428</td>\n",
              "      <td>-1.948883</td>\n",
              "      <td>-0.832498</td>\n",
              "      <td>0.519436</td>\n",
              "      <td>0.903562</td>\n",
              "      <td>1.197315</td>\n",
              "      <td>0.593509</td>\n",
              "      <td>-0.017652</td>\n",
              "      <td>-0.164350</td>\n",
              "      <td>-0.295135</td>\n",
              "      <td>-0.072173</td>\n",
              "      <td>-0.450261</td>\n",
              "      <td>0.313267</td>\n",
              "      <td>-0.289617</td>\n",
              "      <td>0.002988</td>\n",
              "      <td>-0.015309</td>\n",
              "      <td>42.53</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Time        V1        V2  ...       V28  Amount  Class\n",
              "279863  169142.0 -1.927883  1.125653  ...  0.147968  390.00      1\n",
              "280143  169347.0  1.378559  1.289381  ...  0.186637    0.76      1\n",
              "280149  169351.0 -0.676143  1.126366  ...  0.194361   77.89      1\n",
              "281144  169966.0 -3.113832  0.585864  ... -0.253700  245.00      1\n",
              "281674  170348.0  1.991976  0.158476  ... -0.015309   42.53      1\n",
              "\n",
              "[5 rows x 31 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bFsRcj0gX-3M",
        "outputId": "7c6c1b70-d098-4e9c-ad1f-c25f9d91a8d6"
      },
      "source": [
        "new_dataset['Class'].value_counts()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    492\n",
              "0    492\n",
              "Name: Class, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 158
        },
        "id": "jan1xMeWYLrM",
        "outputId": "a944d4b6-b4b7-4949-a112-00ad583eab13"
      },
      "source": [
        "new_dataset.groupby('Class').mean()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Time</th>\n",
              "      <th>V1</th>\n",
              "      <th>V2</th>\n",
              "      <th>V3</th>\n",
              "      <th>V4</th>\n",
              "      <th>V5</th>\n",
              "      <th>V6</th>\n",
              "      <th>V7</th>\n",
              "      <th>V8</th>\n",
              "      <th>V9</th>\n",
              "      <th>V10</th>\n",
              "      <th>V11</th>\n",
              "      <th>V12</th>\n",
              "      <th>V13</th>\n",
              "      <th>V14</th>\n",
              "      <th>V15</th>\n",
              "      <th>V16</th>\n",
              "      <th>V17</th>\n",
              "      <th>V18</th>\n",
              "      <th>V19</th>\n",
              "      <th>V20</th>\n",
              "      <th>V21</th>\n",
              "      <th>V22</th>\n",
              "      <th>V23</th>\n",
              "      <th>V24</th>\n",
              "      <th>V25</th>\n",
              "      <th>V26</th>\n",
              "      <th>V27</th>\n",
              "      <th>V28</th>\n",
              "      <th>Amount</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Class</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>96783.638211</td>\n",
              "      <td>-0.053037</td>\n",
              "      <td>0.055150</td>\n",
              "      <td>-0.036786</td>\n",
              "      <td>-0.046439</td>\n",
              "      <td>0.077614</td>\n",
              "      <td>-0.023218</td>\n",
              "      <td>-0.000703</td>\n",
              "      <td>-0.057620</td>\n",
              "      <td>-0.053438</td>\n",
              "      <td>0.006904</td>\n",
              "      <td>0.003593</td>\n",
              "      <td>-0.013208</td>\n",
              "      <td>0.020052</td>\n",
              "      <td>0.081527</td>\n",
              "      <td>-0.044844</td>\n",
              "      <td>0.028877</td>\n",
              "      <td>0.006312</td>\n",
              "      <td>0.009006</td>\n",
              "      <td>-0.020251</td>\n",
              "      <td>0.060121</td>\n",
              "      <td>0.017306</td>\n",
              "      <td>0.024803</td>\n",
              "      <td>-0.002469</td>\n",
              "      <td>0.036235</td>\n",
              "      <td>-0.061546</td>\n",
              "      <td>0.005988</td>\n",
              "      <td>-0.027930</td>\n",
              "      <td>0.004996</td>\n",
              "      <td>91.477053</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>80746.806911</td>\n",
              "      <td>-4.771948</td>\n",
              "      <td>3.623778</td>\n",
              "      <td>-7.033281</td>\n",
              "      <td>4.542029</td>\n",
              "      <td>-3.151225</td>\n",
              "      <td>-1.397737</td>\n",
              "      <td>-5.568731</td>\n",
              "      <td>0.570636</td>\n",
              "      <td>-2.581123</td>\n",
              "      <td>-5.676883</td>\n",
              "      <td>3.800173</td>\n",
              "      <td>-6.259393</td>\n",
              "      <td>-0.109334</td>\n",
              "      <td>-6.971723</td>\n",
              "      <td>-0.092929</td>\n",
              "      <td>-4.139946</td>\n",
              "      <td>-6.665836</td>\n",
              "      <td>-2.246308</td>\n",
              "      <td>0.680659</td>\n",
              "      <td>0.372319</td>\n",
              "      <td>0.713588</td>\n",
              "      <td>0.014049</td>\n",
              "      <td>-0.040308</td>\n",
              "      <td>-0.105130</td>\n",
              "      <td>0.041449</td>\n",
              "      <td>0.051648</td>\n",
              "      <td>0.170575</td>\n",
              "      <td>0.075667</td>\n",
              "      <td>122.211321</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "               Time        V1        V2  ...       V27       V28      Amount\n",
              "Class                                    ...                                \n",
              "0      96783.638211 -0.053037  0.055150  ... -0.027930  0.004996   91.477053\n",
              "1      80746.806911 -4.771948  3.623778  ...  0.170575  0.075667  122.211321\n",
              "\n",
              "[2 rows x 30 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wbe0g12oYhyK"
      },
      "source": [
        "Splitting the data into Features & Targets"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oiC0OOyUYUoD"
      },
      "source": [
        "X = new_dataset.drop(columns='Class', axis=1)\n",
        "Y = new_dataset['Class']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9u7wbWqzYyrI",
        "outputId": "0c54feb3-2962-4841-f98c-23c4fdb51b76"
      },
      "source": [
        "print(X)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "            Time        V1        V2  ...       V27       V28  Amount\n",
            "203131  134666.0 -1.220220 -1.729458  ...  0.173995 -0.023852  155.00\n",
            "95383    65279.0 -1.295124  0.157326  ...  0.317321  0.105345   70.00\n",
            "99706    67246.0 -1.481168  1.226490  ... -0.546577  0.076538   40.14\n",
            "153895  100541.0 -0.181013  1.395877  ... -0.229857 -0.329608  137.04\n",
            "249976  154664.0  0.475977 -0.573662  ...  0.058961  0.012816   19.60\n",
            "...          ...       ...       ...  ...       ...       ...     ...\n",
            "279863  169142.0 -1.927883  1.125653  ...  0.292680  0.147968  390.00\n",
            "280143  169347.0  1.378559  1.289381  ...  0.389152  0.186637    0.76\n",
            "280149  169351.0 -0.676143  1.126366  ...  0.385107  0.194361   77.89\n",
            "281144  169966.0 -3.113832  0.585864  ...  0.884876 -0.253700  245.00\n",
            "281674  170348.0  1.991976  0.158476  ...  0.002988 -0.015309   42.53\n",
            "\n",
            "[984 rows x 30 columns]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EHnRPzZvYz-F",
        "outputId": "5cd0aae8-1749-4101-a077-35cf5f05b58d"
      },
      "source": [
        "print(Y)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "203131    0\n",
            "95383     0\n",
            "99706     0\n",
            "153895    0\n",
            "249976    0\n",
            "         ..\n",
            "279863    1\n",
            "280143    1\n",
            "280149    1\n",
            "281144    1\n",
            "281674    1\n",
            "Name: Class, Length: 984, dtype: int64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "78wEbV41Y6j3"
      },
      "source": [
        "Split the data into Training data & Testing Data"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FrsqqwT0Y3n5"
      },
      "source": [
        "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FUmwXz99ZuvK",
        "outputId": "a5645b66-417f-4e66-af0f-05cd0a78e182"
      },
      "source": [
        "print(X.shape, X_train.shape, X_test.shape)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "(984, 30) (787, 30) (197, 30)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aowgjqbeZ7d1"
      },
      "source": [
        "Model Training"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "i0NkjaxyZ96E"
      },
      "source": [
        "Logistic Regression"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "i0HHd1v8Z2Mq"
      },
      "source": [
        "model = LogisticRegression()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_rshSouvaGrv",
        "outputId": "bed2be43-222c-41ae-925c-ffac11b7cb52"
      },
      "source": [
        "# training the Logistic Regression Model with Training Data\n",
        "model.fit(X_train, Y_train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
              "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
              "                   multi_class='auto', n_jobs=None, penalty='l2',\n",
              "                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,\n",
              "                   warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "H9FYWyKjalvC"
      },
      "source": [
        "Model Evaluation"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "O6O6kbwYaoxH"
      },
      "source": [
        "Accuracy Score"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pC2kCJhOaage"
      },
      "source": [
        "# accuracy on training data\n",
        "X_train_prediction = model.predict(X_train)\n",
        "training_data_accuracy = accuracy_score(X_train_prediction, Y_train)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ijq6gAevbDwm",
        "outputId": "00f7db4a-a96d-4ee8-f1ff-d9a925aabcbe"
      },
      "source": [
        "print('Accuracy on Training data : ', training_data_accuracy)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Accuracy on Training data :  0.9415501905972046\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tryJUs6mbJM7"
      },
      "source": [
        "# accuracy on test data\n",
        "X_test_prediction = model.predict(X_test)\n",
        "test_data_accuracy = accuracy_score(X_test_prediction, Y_test)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lxEuN24ib3hS",
        "outputId": "b513f28a-352b-4ea1-aa4d-96a873ad6cca"
      },
      "source": [
        "print('Accuracy score on Test Data : ', test_data_accuracy)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Accuracy score on Test Data :  0.9390862944162437\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
