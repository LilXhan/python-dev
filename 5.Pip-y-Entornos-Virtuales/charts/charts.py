import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    values = [200, 34, 120, 400]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('ahora_si_charts_final_de_veritas.png')
    plt.close()
