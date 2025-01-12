# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy dalam spesialisasi _Data Analytics_. Deliverables yang diharapkan dari projek ini adalah melakukan _web scraping_ sederhana untuk mendapatkan informasi. Kita juga akan menggunakan dashboard sederhana Flask untuk menampilkan hasil _scrap_ dan visualisasi.

Untuk panduan langkah demi langkah, Anda dapat membuka repositori Git berikut [di sini](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Web Scraping with Beautiful Soup"). *⚠️ Disclaimer: link di atas akan mengarah ke sebuah direktori GitHub lain yang sama dengan direktori pada [video panduan capstone web scraping](https://drive.google.com/drive/u/4/folders/1GyRYIUgaREwcz5FT76UDNyobLSrnERgw). Namun, kasus yang ada pada direktori GitHub tersebut hanya merupakan contoh agar Bapak/Ibu dapat memahami workflow web scraping, bukan kasus yang akan Bapak/Ibu kerjakan dalam capstone ini. Kasus yang bisa Bapak/Ibu pilih dan kerjakan dapat dilihat pada bagian di bawah ini.*

### The Final Mission

Pada **capstone** kali ini, Anda dapat memilih salah satu dari kasus berikut untuk dikerjakan:

1. [Case Data kurs US Dollar ke rupiah](https://www.exchange-rates.org/exchange-rate-history/usd-idr)

   - Dari halaman tersebut carilah `tanggal`, dan `harga harian`
   - Bualah plot pergerakan kurs USD
# TASK 1 sudah beres
   

2. [Case IMDB Box Office Mojo](https://www.boxofficemojo.com/year/world/)

   - Dari Halaman tersebut carilah kolom `Rank`, `Release Group`, `Worldwide`, `Domestic`, dan `Foreign`
   - Note: kolom `worldwide` merupakan total dari kolom `domestic` dan `foreign`, analisa dan plot bisa disesuaikan.
   - Buatlah plot dari 10 film paling populer di tahun 2024

3. [Case Berita Detik.com tentang Gempa](https://www.detik.com/search/searchall?query=gempa)
   - Dari halaman tersebut carilah `judul`, `berita` , dan `tanggal`
   - Bualah word cloud dari judul. hint: gunakan bantuan `.str.cat()`

Happy Learning!
