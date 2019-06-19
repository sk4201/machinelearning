{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "19june-2.py",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sk4201/machinelearning/blob/master/19june_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X6itdT7MKnhq",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "C2x-2P4ZLQwa",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# reading data from a csv file\n",
        "\n",
        "df=pd.read_csv('com.csv')\n",
        "#df1=pd.read_csv(\"http://13.234.66.67/summer19/datasets/bank.csv\")"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "u6DVSrRGLotl",
        "colab_type": "code",
        "outputId": "d18558b1-cc54-4674-d40b-809fcece3a93",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 170
        }
      },
      "source": [
        "#data structure\n",
        "df.info()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 6 entries, 0 to 5\n",
            "Data columns (total 4 columns):\n",
            "Name          6 non-null object\n",
            "Department    4 non-null object\n",
            "Manager       4 non-null object\n",
            "Salary        6 non-null int64\n",
            "dtypes: int64(1), object(3)\n",
            "memory usage: 272.0+ bytes\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tuhEpG4LMHXU",
        "colab_type": "code",
        "outputId": "710c3303-e339-4a4f-bdcb-76852283b5da",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        }
      },
      "source": [
        "# toprint all  the data\n",
        "df"
      ],
      "execution_count": 0,
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
              "      <th>Name</th>\n",
              "      <th>Department</th>\n",
              "      <th>Manager</th>\n",
              "      <th>Salary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Arsene Wenger</td>\n",
              "      <td>Bar</td>\n",
              "      <td>Friar Tuck</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Friar Tuck</td>\n",
              "      <td>Foo</td>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Little John</td>\n",
              "      <td>Foo</td>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Sam Allardyce</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>250</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Dimi Berbatov</td>\n",
              "      <td>Foo</td>\n",
              "      <td>Little John</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Name Department      Manager  Salary\n",
              "0     Robin Hood        NaN          NaN     200\n",
              "1  Arsene Wenger        Bar   Friar Tuck      50\n",
              "2     Friar Tuck        Foo   Robin Hood     100\n",
              "3    Little John        Foo   Robin Hood     100\n",
              "4  Sam Allardyce        NaN          NaN     250\n",
              "5  Dimi Berbatov        Foo  Little John      50"
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
      "cell_type": "code",
      "metadata": {
        "id": "ziVxzVQEM9T2",
        "colab_type": "code",
        "outputId": "ffd2f544-685d-4357-e08f-078dc21758d6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 142
        }
      },
      "source": [
        "# top 3 rows\n",
        "df.head(3)"
      ],
      "execution_count": 0,
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
              "      <th>Name</th>\n",
              "      <th>Department</th>\n",
              "      <th>Manager</th>\n",
              "      <th>Salary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>NaN</td>\n",
              "      <td>NaN</td>\n",
              "      <td>200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Arsene Wenger</td>\n",
              "      <td>Bar</td>\n",
              "      <td>Friar Tuck</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Friar Tuck</td>\n",
              "      <td>Foo</td>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Name Department     Manager  Salary\n",
              "0     Robin Hood        NaN         NaN     200\n",
              "1  Arsene Wenger        Bar  Friar Tuck      50\n",
              "2     Friar Tuck        Foo  Robin Hood     100"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "soZ89DdkNHJ3",
        "colab_type": "code",
        "outputId": "f1dc3ed6-7276-4dcf-f0d3-cb1904faa9e0",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 80
        }
      },
      "source": [
        "# from down 1 rows\n",
        "df.tail(1)"
      ],
      "execution_count": 0,
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
              "      <th>Name</th>\n",
              "      <th>Department</th>\n",
              "      <th>Manager</th>\n",
              "      <th>Salary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Dimi Berbatov</td>\n",
              "      <td>Foo</td>\n",
              "      <td>Little John</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Name Department      Manager  Salary\n",
              "5  Dimi Berbatov        Foo  Little John      50"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SpTg5xuHNWro",
        "colab_type": "code",
        "outputId": "1023b3a8-c8a3-4043-b1b4-19557b9d68a9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        }
      },
      "source": [
        "# for particular column\n",
        "\n",
        "df['Name']"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       Robin Hood\n",
              "1    Arsene Wenger\n",
              "2       Friar Tuck\n",
              "3      Little John\n",
              "4    Sam Allardyce\n",
              "5    Dimi Berbatov\n",
              "Name: Name, dtype: object"
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
        "id": "ycu8XXU4NiVh",
        "colab_type": "code",
        "outputId": "36a26e69-9618-4783-d3a5-54bf46810d22",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        }
      },
      "source": [
        "# for selecting rows and column\n",
        "df.iloc[0:,0]"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       Robin Hood\n",
              "1    Arsene Wenger\n",
              "2       Friar Tuck\n",
              "3      Little John\n",
              "4    Sam Allardyce\n",
              "5    Dimi Berbatov\n",
              "Name: Name, dtype: object"
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
        "id": "TQmIBmEmOHR3",
        "colab_type": "code",
        "outputId": "9dac08e6-8f38-4c49-87ae-12b7c1b5bc28",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        }
      },
      "source": [
        "df.iloc[0:,0:2]"
      ],
      "execution_count": 0,
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
              "      <th>Name</th>\n",
              "      <th>Department</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Arsene Wenger</td>\n",
              "      <td>Bar</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Friar Tuck</td>\n",
              "      <td>Foo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Little John</td>\n",
              "      <td>Foo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Sam Allardyce</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Dimi Berbatov</td>\n",
              "      <td>Foo</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Name Department\n",
              "0     Robin Hood        NaN\n",
              "1  Arsene Wenger        Bar\n",
              "2     Friar Tuck        Foo\n",
              "3    Little John        Foo\n",
              "4  Sam Allardyce        NaN\n",
              "5  Dimi Berbatov        Foo"
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
      "cell_type": "code",
      "metadata": {
        "id": "pD-JErJoOOCW",
        "colab_type": "code",
        "outputId": "f15e5322-7db0-4b0c-a994-5e96ff2e1ed9",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 235
        }
      },
      "source": [
        "df.iloc[0:,[0,3]]"
      ],
      "execution_count": 0,
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
              "      <th>Name</th>\n",
              "      <th>Salary</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Robin Hood</td>\n",
              "      <td>200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Arsene Wenger</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Friar Tuck</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Little John</td>\n",
              "      <td>100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Sam Allardyce</td>\n",
              "      <td>250</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Dimi Berbatov</td>\n",
              "      <td>50</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "            Name  Salary\n",
              "0     Robin Hood     200\n",
              "1  Arsene Wenger      50\n",
              "2     Friar Tuck     100\n",
              "3    Little John     100\n",
              "4  Sam Allardyce     250\n",
              "5  Dimi Berbatov      50"
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
        "id": "V0mg3n6gOlcP",
        "colab_type": "code",
        "outputId": "55783050-4565-4853-e33e-1cd4783e8029",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 136
        }
      },
      "source": [
        "#salary column\n",
        "df[\"Salary\"]\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    200\n",
              "1     50\n",
              "2    100\n",
              "3    100\n",
              "4    250\n",
              "5     50\n",
              "Name: Salary, dtype: int64"
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
        "id": "UuknQQCcPEGv",
        "colab_type": "code",
        "outputId": "c7992384-63d0-47e7-baea-7c76fadca6b8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "df[\"Salary\"].max() #it take out the maxium salary"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "250"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OO1aQjMSPjbe",
        "colab_type": "code",
        "outputId": "b59b4f33-0538-49d1-c764-23851442a472",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "df[\"Salary\"].mean()  #it take out the mean salary"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "125.0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RyMe4Z0yPp8x",
        "colab_type": "code",
        "outputId": "92ba5e06-41d5-4328-d01c-d678c96398bf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "df[\"Salary\"].sum() #it take out the sum of salary"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "750"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NQGSA7WpPyON",
        "colab_type": "code",
        "outputId": "ec596292-6bcb-40d2-e40f-4a6f9e164a60",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "x=df\n",
        "type(x)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "pandas.core.frame.DataFrame"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p9Czmgo7Qhm0",
        "colab_type": "code",
        "outputId": "cf0489e5-53f6-4377-d766-340d89b1a3c8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "x=df.values\n",
        "type(x)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "numpy.ndarray"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TZt8U2T3QsYn",
        "colab_type": "code",
        "outputId": "22182046-b99c-42bb-d124-ec6cc04e5037",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "# we donot want index number in the for of array\n",
        "\n",
        "df[\"Salary\"].values"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([200,  50, 100, 100, 250,  50])"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "49a18pXpQ_qt",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}