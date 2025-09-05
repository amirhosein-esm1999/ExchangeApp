import matplotlib.pyplot as plt


def show_bar(df):
    fig, ax = plt.subplots()
    ax.bar(df["Currency"], df["ExchangeRate"], color="#0a7c84")
    ax.set_title("Exchange Rates (USD-based)")
    ax.set_xlabel("Currency")
    ax.set_ylabel("Rates")
    plt.tight_layout()
    return fig