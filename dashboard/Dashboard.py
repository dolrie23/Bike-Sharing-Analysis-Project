import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style("dark")

# Inisiasi

st.title("US Bike Sharing Analysis🚲")
st.sidebar.title("Menu Analisis")
st.sidebar.header("Pilih Tipe Analisisnya!")
uploaded_data = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Daftar opsi analisis data
choice = st.sidebar.selectbox(
    'Pilih Analisis yang Ingin Dilihat:',
    [
        'How Seasonal and Weather Changes Affect Our User?',
        'Weekday vs Weekend',
        'When we need promotion?',
    ]
)
if uploaded_data is not None:
    df = pd.read_csv(uploaded_data)
    st.write('🚲 Here is: The Dataset Preview 🚲')
    st.dataframe(df.head(10))

    if choice == 'How Seasonal and Weather Changes Affect Our User?':
        st.header("Pengaruh Musim dan Cuaca terhadap User")

        # Code for visualization
        # retrieve seasonal data
        seasonal = df.groupby('Season').agg({
            'Casual': 'sum',
            'Registered': 'sum',
            'Total User': 'sum'
        })
        # retrieve weather data
        weather = df.groupby(['Weather']).agg({
            'Casual': 'sum',
            'Registered': 'sum',
            'Total User': 'sum'
        })

        # Initiation for plot
        bar_width = 0.25
        x_season = np.arange(len(seasonal))
        x_weather = np.arange(len(weather))
        season_list = seasonal.index.tolist()
        weather_list = weather.index.tolist()

        fig, axes = plt.subplots(1, 2, figsize=(12, 6))

        # Plot untuk Season
        axes[0].bar(x_season, seasonal['Casual'], width=bar_width, label='Casual', color='cyan', align='center')
        axes[0].bar(x_season + bar_width, seasonal['Registered'], width=bar_width, label='Registered', color='red',
                    align='center')
        axes[0].bar(x_season + 2 * bar_width, seasonal['Total User'], width=bar_width, label='Total User',
                    color='green', align='center')

        axes[0].set_title('Pengaruh Season terhadap User', size=15)
        axes[0].set_xlabel('Season')
        axes[0].set_ylabel('User')
        axes[0].set_xticks(x_season)
        axes[0].set_xticklabels(season_list)
        axes[0].legend()
        axes[0].grid()

        # Plot untuk Weather
        axes[1].bar(x_weather, weather['Casual'], width=bar_width, label='Casual', color='cyan', align='center')
        axes[1].bar(x_weather + bar_width, weather['Registered'], width=bar_width, label='Registered', color='red',
                    align='center')
        axes[1].bar(x_weather + 2 * bar_width, weather['Total User'], width=bar_width, label='Total User',
                    color='green', align='center')

        axes[1].set_title('Pengaruh Weather terhadap User', size=15)
        axes[1].set_xlabel('Weather')
        axes[1].set_ylabel('User')
        axes[1].set_xticks(x_weather + bar_width)
        axes[1].set_xticklabels(weather_list)
        axes[1].legend()
        axes[1].grid()

        # Plot the Result
        plt.tight_layout()
        st.pyplot(fig)

        st.subheader('Hasil Analisis')
        st.markdown('''
        Berdasarkan Visualisasi diatas dapat dilihat bahwa grafik yang ada di sebelah kiri menunjukkan
        pengaruh musim terhadap user sedangkan yang di sebelah kanan adalah grafik yang menunjukkan pengaruh cuaca
        terhadap user. Kondisi yang paling membawa benefit bagi US Bike Sharing adalah saat musim Gugur (📉) dan saat cuaca
        Baik (🌤⛅🌥). Tercatat bahwa saat musim gugur terdapat Total 1.061.129 user dan saat cuaca baik Total 2.338.173 user.
        
        Hal yang sangat signifikan perbedaannya jika dibandingkan dengan saat musim semi total user hanya tercatat 
        471.348 user dan saat cuaca Buruk tercatat 223 user. Hal tersebut juga sejalan dengan perbandingan antara
        grafik casual user dan registered user yang memiliki karakteristik yang serupa dengan Total User.''')

    elif choice == 'Weekday vs Weekend':
        st.header("Perilaku User pada hari kerja vs akhir pekan")

        workingday_data = df[df['Workdays'] == 'Yes']
        weekend_data = df[df['Workdays'] == 'No']

        # Casual User
        workingday_avg_casual = workingday_data.groupby('Hour')['Casual'].mean().reset_index()
        weekend_avg_casual = weekend_data.groupby('Hour')['Casual'].mean().reset_index()

        # Registered User
        workingday_avg_registered = workingday_data.groupby('Hour')['Registered'].mean().reset_index()
        weekend_avg_registered = weekend_data.groupby('Hour')['Registered'].mean().reset_index()

        # Total User
        workingday_avg_total = workingday_data.groupby('Hour')['Total User'].mean().reset_index()
        weekend_avg_total = weekend_data.groupby('Hour')['Total User'].mean().reset_index()

        st.subheader('Plot 1')
        fig, ax = plt.subplots(figsize=(12, 6))

        sns.lineplot(x='Hour', y='Casual', data=workingday_avg_casual, label='Workday_C', color='blue', marker='o')
        sns.lineplot(x='Hour', y='Casual', data=weekend_avg_casual, label='Weekend_C', color='red', marker='o',)
        ax.set_title('Working Day vs Weekend Users', size=15)
        ax.set_xlabel('Hour')
        ax.set_xticks(range(0, 24))
        ax.set_ylabel('Number of Casual Users')
        ax.grid()
        ax.legend()

        st.pyplot(fig)

        st.subheader('Plot 2')
        fig, ax = plt.subplots(figsize=(12, 6))

        sns.lineplot(x='Hour', y='Registered', data=workingday_avg_registered, label='Workday_R', color='blue',
                     marker='o', )
        sns.lineplot(x='Hour', y='Registered', data=weekend_avg_registered, label='Weekend_R', color='red', marker='o')
        ax.set_title('Working Day vs Weekend Users', size=15)
        ax.set_xlabel('Hour')
        ax.set_xticks(range(0, 24))
        ax.set_ylabel('Number of Casual Users')
        ax.grid()
        ax.legend()

        st.pyplot(fig)

        st.subheader('Plot 3')
        fig, ax = plt.subplots(figsize=(12, 6))

        sns.lineplot(x='Hour', y='Total User', data=workingday_avg_total, label='Workday_T', color='blue', marker='o')
        sns.lineplot(x='Hour', y='Total User', data=weekend_avg_total, label='Weekend_T', color='red', marker='o')
        ax.set_title('Working Day vs Weekend Users', size=15)
        ax.set_xlabel('Hour')
        ax.set_xticks(range(0, 24))
        ax.set_ylabel('Number of Casual Users')
        ax.grid()
        ax.legend()

        st.pyplot(fig)

        st.subheader('Hasil Analisis')
        st.markdown('''
        1. Melalui plot 1, ditemukan bahwa user casual aktif paling tinggi saat weekend. Hal tersebut terlihat dengan titik puncak pada user casual ada pada saat weekend di jam 14.00 dengan rerata pengguna sebesar 140 pengguna.  
        2. Melalui plot 2, ditemukan bahwa user registered aktif paling tinggi di saat weekday terutama di jam 08.00 dan jam 17.00 dengan rerata pengguna berturut-turut sebesar 454, dan 468 pengguna. Dapat disimpulkan bahwa pengguna registered dominan menggunakan bike sharing saat jam sibuk.
        2. Melalui plot 3 dapat juga disimpulkan bahwa perilaku user bike sharing pada saat workday cenderung menyerupai user registered. Hal tersebut disebabkan oleh user casual yang lebih sedikit daripada user registered. Sedangkan pada weekend, keseluruhan user cenderung stabil kenaikan user yaitu meningkat mulai jam 07.00 (rerata 43 pengguna) hingga pada puncaknya jam 12.00 (rerata 366 pengguna) dan menurun setelah jam 16.00 (rerata 353 pengguna). Hal tersebut tergolong wajar karena pengguna yang menunjukkan hanya menggunakan bike sharing untuk mobilisasi santai di akhir pekan.
        ''')

    elif choice == 'When we need promotion?':
        st.header("Korelasi setiap atribut data terhadap Jumlah User")

        casual = df.Casual.sum()
        registered = df.Registered.sum()

        user_type = ['Casual', 'Registered']
        datas = [casual, registered]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(user_type, datas, label='Casual', color=['cyan', 'maroon'], align='center')
        ax.set_xlabel('Users')
        ax.set_ylabel('User Type')
        ax.set_title('Casual Vs Registered Users', size=15)
        for i, value in enumerate(datas):
            ax.text(i, value + 10000, f'{value:,}', ha='center', va='bottom')

        st.pyplot(fig)
        st.subheader('Hasil Analisis')
        st.markdown('''
        Berdasarkan distribusi pengguna diatas, dapat diketahui perbedaan yang cukup jauh antara user casual dengan registered. 
        Dimana tercatat total user tipe casual di tahun 2011 dan 2012 adalah 620.017 dan user tipe registered sebesar 2.672.662 pengguna. 
        ''')
else:
    st.write("Please upload a CSV file to start analyzing the data.")