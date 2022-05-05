import matplotlib.pyplot as plt
def pie_chart(df, columnnames):
    for i in columnnames:
        plt.figure()
        df.loc[:,i].plot.pie(figsize = (12,10), autopct='%1.1f%%',legend = None, ylabel = "", title = i)