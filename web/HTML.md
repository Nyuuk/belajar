# Daftar Isi
- [Daftar Isi](#daftar-isi)
- [Introduction to HTML](#introduction-to-html)
    - [Apa itu HTML?](#h1-s1)
    - [Struktur dasar HTML](#h1-s2)
    - [Tag dan Elemen HTML](#tag-dan-elemen-html)
    - [Atribut HTML](#atribut-html)
- [Membangun Struktur Halaman](#membangun-struktur-halaman)
    - [Menggunakan Tag html, head dan body](#menggunakan-tag-html-head-dan-body)
    - [Menambahkan judul halaman dengan tag title](#menambahkan-judul-halaman-dengan-tag-title)
    - [Membuat Paragraf dengan tag p](#membuat-paragraf-dengan-tag-p)
    - [Membuat Heading dengan tag h1 hinggan h6](#membuat-heading-dengan-tag-h1-hinggan-h6)
    - [Membuat tautan dengan tag a](#membuat-tautan-dengan-tag-a)
- [Mengelompokan dan Mengatur Konten](#mengelompokan-dan-mengatur-konten)
    - [Menggunakan tag div untuk membuat blok konten](#menggunakan-tag-div-untuk-membuat-blok-konten)
    - [Menggunakan tag span untuk menandai bagian kecil dari teks](#menggunakan-tag-span-untuk-menandai-bagian-kecil-dari-teks)
    - [Membuat daftar menggunakan tag ul, ol, dan li](#membuat-daftar-dengan-tag-ul-ol-dan-li)
    - [Membuat tabel dengan tag table, tr, th dan td](#membuat-tabel-dengan-tag-table-tr-th-dan-td)
- [Menampilkan Gambar dan Media](#menampilkan-gambar-dan-media)
    - [Menambahkan gambar dengan tag img](#menambahkan-gambar-dengan-tag-img)
    - [Menambahkan Video dengan tag video](#menambahkan-video-dengan-tag-video)
    - [Menambahkan Audio dengan tag audio](#menambahkan-audio-dengan-tag-audio)
    - [Menambahkan konten lain dengan tag iframe](#menambahkan-konten-lain-dengan-tag-iframe)
    - [Menggunakan tag figure dan figcaption](#menggunakan-tag-figure-dan-figcaption)
- [Membuat Fromulir](#membuat-formulir)
    - [Menggunakan tag form untuk membuat Formulir](#menggunakan-tag-form-untuk-membuat-formulir)
    - [Menambahkan bidang masukan dengan tag input](#menambahkan-bidang-masukan-dengan-tag-input)
    - [Menggunakan tag textarea untuk memasukan teks panjang](#menggunakan-tag-textarea-untuk-memasukkan-teks-panjang)
    - [Menggunakan tag select dan option untuk membuat menu dropdown](#menggunakan-tag-select-dan-option-untuk-membuat-menu-dropdown)
- [Penutup](#penutup)

---
# Introduction to HTML
> Pengenalan HTML | menuasai Fundamentaal Front End Bagi pemula
---
## Apa itu HTML? <a id="h1-s1"></a>
HTML, singkatan dari HyperText Markup Language, adalah bahasa markah standar yang digunakan untuk membuat dan mengatur struktur konten pada halaman web. HTML menggunakan elemen-elemen markup (tag) untuk menandai dan mengelompokkan konten seperti teks, gambar, tautan, tabel, dan lainnya, sehingga memungkinkan browser web untuk menginterpretasikan dan menampilkan konten tersebut dengan benar kepada pengguna.

Berikut ini penjelasan lebih rinci tentang HTML:

1. HyperText:
   HTML memungkinkan pembuatan dan penggunaan hyperlink, yang memungkinkan pengguna untuk berpindah antara halaman web dengan mengklik tautan. Hyperlink ini memungkinkan para pengguna menjelajahi dan menavigasi situs web dengan mudah.

2. Markup Language:
   HTML adalah bahasa markah yang menggunakan elemen-elemen markup untuk menandai konten pada halaman web. Elemen markup didefinisikan oleh tag, yang terdiri dari tanda kurung sudut (< dan >) yang mengelilingi teks tertentu. Tag ini memberi tahu browser bagaimana konten tersebut harus ditampilkan dan diinterpretasikan.

3. Struktur Konten:
   HTML digunakan untuk mengatur dan mengelompokkan konten pada halaman web. Dengan HTML, Anda dapat menentukan judul halaman, membuat paragraf, membuat heading, membuat daftar, menampilkan gambar, membuat tabel, membuat formulir, dan banyak lagi. HTML memberi struktur pada konten sehingga lebih mudah dipahami dan ditampilkan oleh browser.

4. Tidak Memiliki Fungsi Pemrograman:
   HTML bukanlah bahasa pemrograman, melainkan bahasa markah. Ini berarti bahwa HTML tidak memiliki kemampuan untuk melakukan operasi logika atau interaksi dinamis di dalam halaman web. Untuk membuat halaman web yang interaktif dan dinamis, Anda perlu menggunakan bahasa pemrograman seperti JavaScript.

5. Kompatibilitas dengan Browser:
   HTML didukung oleh hampir semua browser web yang ada, sehingga halaman web yang dibuat dengan HTML dapat ditampilkan secara konsisten di berbagai perangkat dan platform.

6. Versi HTML:
   HTML telah berkembang dari waktu ke waktu dengan munculnya versi-versi baru. Versi yang paling umum digunakan saat ini adalah HTML5, yang memperkenalkan banyak fitur baru dan perbaikan dibandingkan dengan versi sebelumnya.

7. Mendukung CSS dan JavaScript:
   HTML bekerja sama dengan bahasa lain seperti CSS (Cascading Style Sheets) dan JavaScript. CSS digunakan untuk mengatur tampilan dan gaya halaman web, sedangkan JavaScript digunakan untuk membuat interaksi dan logika yang lebih kompleks.

HTML adalah dasar dalam pembuatan halaman web. Dengan menggunakan tag dan elemen HTML, Anda dapat membangun struktur konten yang terorganisir dan tampilan yang sesuai. HTML bekerja sama dengan CSS dan JavaScript untuk menciptakan pengalaman pengguna yang lebih baik dan interaktif di web.

Mengerti HTML adalah langkah pertama yang penting dalam mempelajari pengembangan web. Dengan memahami konsep dan sintaksis HTML, Anda dapat membangun halaman web dasar dan melanjutkan untuk mempelajari aspek lain seperti CSS dan JavaScript.

---
## Struktur dasar HTML <a id="h1-s2"></a>
HTML memiliki struktur dasar yang terdiri dari beberapa elemen penting yang membentuk kerangka kerja sebuah halaman web. Struktur ini terdiri dari elemen `<html>`, `<head>`, dan `<body>`. Mari kita jelaskan masing-masing elemen ini secara rinci:

1. Elemen `<html>`:
   - Elemen `<html>` adalah elemen utama yang membungkus seluruh konten halaman web.
   - Setiap halaman HTML harus dimulai dengan elemen `<html>` dan diakhiri dengan elemen `</html>`.
   - Isi dari halaman web ditempatkan di antara elemen `<html>` dan `</html>`.
   - Contoh penggunaan elemen `<html>`:

   ```html
   <html>
     <!-- Isi halaman web -->
   </html>
   ```

2. Elemen `<head>`:
   - Elemen `<head>` berisi informasi tentang dokumen HTML seperti judul halaman, tautan ke stylesheet, dan metadata lainnya.
   - Konten yang ada di dalam elemen `<head>` tidak akan ditampilkan di halaman web itu sendiri, tetapi memberikan informasi penting kepada browser dan mesin pencari.
   - Contoh penggunaan elemen `<head>`:

   ```html
   <html>
     <head>
       <!-- Informasi tentang dokumen HTML -->
     </head>
     <body>
       <!-- Konten halaman web -->
     </body>
   </html>
   ```

3. Elemen `<body>`:
   - Elemen `<body>` berisi semua konten yang akan ditampilkan di halaman web, seperti teks, gambar, tautan, tabel, formulir, dan lainnya.
   - Konten yang ada di dalam elemen `<body>` akan ditampilkan secara visual di halaman web.
   - Contoh penggunaan elemen `<body>`:

   ```html
   <html>
     <head>
       <!-- Informasi tentang dokumen HTML -->
     </head>
     <body>
       <!-- Konten halaman web -->
     </body>
   </html>
   ```

Jadi, struktur dasar HTML terdiri dari tiga elemen utama: `<html>`, `<head>`, dan `<body>`. Elemen `<html>` adalah elemen utama yang membungkus seluruh konten halaman web. Elemen `<head>` berisi informasi tentang dokumen HTML, sementara elemen `<body>` berisi konten yang akan ditampilkan di halaman web.

Dengan memahami struktur dasar HTML ini, Anda dapat memulai membuat halaman web sederhana. Selanjutnya, Anda dapat menambahkan elemen-elemen HTML lainnya ke dalam elemen `<body>` untuk membangun tampilan dan fungsionalitas yang lebih kompleks.

---
## Tag dan elemen HTML
HTML (HyperText Markup Language) digunakan untuk membuat halaman web. Dalam HTML, kita menggunakan tag dan elemen untuk mengatur struktur dan konten halaman web.

- Tag HTML: Tag HTML adalah instruksi yang digunakan untuk memberi tahu browser bagaimana cara mengatur dan menampilkan konten di halaman web. Tag HTML umumnya ditulis dalam format `<tag>konten</tag>`. Misalnya, tag `<h1>` digunakan untuk judul utama, tag `<p>` digunakan untuk paragraf, dan tag `<a>` digunakan untuk membuat tautan.

- Elemen HTML: Elemen HTML adalah kombinasi dari tag HTML beserta kontennya. Sebuah elemen dimulai dengan tag pembuka dan diakhiri dengan tag penutup. Misalnya, elemen `<h1>` akan terlihat seperti `<h1>Judul Utama</h1>`. Elemen juga dapat memiliki atribut yang memberikan informasi tambahan tentang elemen tersebut, seperti atribut `src` pada tag `<img>` yang digunakan untuk menentukan sumber gambar.

- Struktur Dasar HTML: Setiap halaman HTML biasanya dimulai dengan tag `<html>` sebagai kontainer utama. Di dalam `<html>`, terdapat tag `<head>` yang berisi informasi tentang halaman seperti judul dan tautan ke file CSS. Selanjutnya, tag `<body>` digunakan untuk mengandung konten utama halaman seperti teks, gambar, dan elemen-elemen lainnya.

Contoh sederhana penggunaan tag dan elemen HTML:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Halaman Web Sederhana</title>
</head>
<body>
  <h1>Selamat Datang!</h1>
  <p>Ini adalah halaman web sederhana.</p>
  <img src="gambar.jpg" alt="Gambar">
  <a href="https://www.example.com">Kunjungi Situs Web</a>
</body>
</html>
```

Pada contoh di atas, kita menggunakan tag `<h1>` untuk judul utama, tag `<p>` untuk paragraf teks, tag `<img>` untuk menampilkan gambar, dan tag `<a>` untuk membuat tautan ke situs web lain.

Dengan menggunakan tag dan elemen HTML, kita dapat mengatur struktur dan konten halaman web dengan mudah.
## Atribut HTML
Dalam HTML, atribut digunakan untuk memberikan informasi tambahan tentang elemen HTML. Atribut berfungsi untuk mengontrol perilaku atau tampilan dari elemen tersebut.

- Atribut HTML: Atribut HTML ditempatkan di dalam tag HTML dan memberikan nilai tambahan kepada elemen tersebut. Atribut biasanya terdiri dari pasangan "nama atribut" dan "nilai atribut" yang diberikan dalam format `nama_atribut="nilai_atribut"`. Misalnya, atribut `src` pada tag `<img>` digunakan untuk menentukan sumber gambar, dan atribut `href` pada tag `<a>` digunakan untuk menentukan tujuan tautan.

- Contoh penggunaan atribut HTML: Berikut adalah contoh penggunaan atribut dalam elemen HTML.

```html
<a href="https://www.example.com" target="_blank">Kunjungi Situs Web</a>
<img src="gambar.jpg" alt="Gambar" width="300" height="200">
<input type="text" id="nama" placeholder="Masukkan Nama">
```

Pada contoh di atas, kita menggunakan atribut `href` dengan nilai `"https://www.example.com"` dan `target` dengan nilai `"_blank"` pada tag `<a>` untuk membuat tautan yang membuka situs web dalam tab baru. Pada tag `<img>`, kita menggunakan atribut `src` untuk menentukan sumber gambar, atribut `alt` untuk memberikan teks alternatif jika gambar tidak dapat ditampilkan, serta atribut `width` dan `height` untuk mengatur ukuran gambar. Pada tag `<input>`, kita menggunakan atribut `type` untuk menentukan jenis input, atribut `id` untuk memberikan identifikasi unik, dan atribut `placeholder` untuk memberikan teks petunjuk.

Dengan menggunakan atribut HTML, kita dapat mengontrol perilaku dan tampilan elemen HTML sesuai dengan kebutuhan kita.

---
# Membangun Struktur Halaman
Ketika Anda membuat halaman web, penting untuk membangun struktur yang baik. Struktur ini membantu browser dan mesin pencari memahami konten Anda dengan benar. Berikut adalah langkah-langkah dalam membangun struktur HTML:

---
## Menggunakan tag html, head dan body
1. Mulailah dengan tag `<html>`:
   - Tag `<html>` digunakan sebagai elemen utama yang membungkus seluruh konten halaman web.
   - Setiap halaman HTML harus dimulai dengan tag `<html>` dan diakhiri dengan tag `</html>`.
   - Semua elemen halaman web akan berada di antara tag `<html>` dan `</html>`.
   - Contoh penggunaan tag `<html>`:

   ```html
   <html>
     <!-- Konten halaman web -->
   </html>
   ```

2. Gunakan tag `<head>`:
   - Tag `<head>` berada di dalam tag `<html>` dan digunakan untuk menyediakan informasi tentang dokumen HTML.
   - Konten yang ada di dalam tag `<head>` tidak akan ditampilkan secara visual di halaman web, tetapi memberikan informasi penting kepada browser dan mesin pencari.
   - Contoh penggunaan tag `<head>`:

   ```html
   <html>
     <head>
       <!-- Informasi tentang dokumen HTML -->
     </head>
     <!-- Konten halaman web -->
   </html>
   ```

3. Gunakan tag `<body>`:
   - Tag `<body>` juga berada di dalam tag `<html>` dan berfungsi untuk menampilkan konten yang akan ditampilkan secara visual di halaman web.
   - Semua elemen seperti teks, gambar, tautan, tabel, formulir, dan lainnya ditempatkan di dalam tag `<body>`.
   - Contoh penggunaan tag `<body>`:

   ```html
   <html>
     <head>
       <!-- Informasi tentang dokumen HTML -->
     </head>
     <body>
       <!-- Konten halaman web -->
     </body>
   </html>
   ```

Dengan memahami langkah-langkah tersebut, Anda dapat membangun struktur dasar sebuah halaman web menggunakan tag `<html>`, `<head>`, dan `<body>`. Tag `<html>` menjadi elemen utama yang membungkus seluruh konten halaman web. Tag `<head>` menyediakan informasi tentang dokumen HTML, sedangkan tag `<body>` menampilkan konten yang akan ditampilkan secara visual di halaman web.

Jangan lupa bahwa elemen-elemen HTML lainnya, seperti tag `<h1>`, `<p>`, `<a>`, `<img>`, dan lainnya, akan ditempatkan di dalam tag `<body>` untuk membangun struktur dan konten halaman web yang lebih kompleks.

---
## Menambahkan judul halaman dengan tag title
Judul halaman adalah teks yang ditampilkan di bilah judul atau tab browser. Tag `<title>` digunakan untuk menentukan judul halaman web Anda. Berikut adalah langkah-langkah untuk menambahkan judul halaman menggunakan tag `<title>`:

1. Buka tag `<head>` dalam dokumen HTML Anda.
2. Tambahkan tag `<title>` di dalam tag `<head>`.
3. Tulis judul halaman web Anda antara tag pembuka `<title>` dan penutup `</title>`.
4. Simpan judul yang Anda tulis dalam beberapa kata yang relevan dengan halaman web Anda.
5. Tag `<title>` harus berada di atas tag `<body>`, tetapi di dalam tag `<head>`.

Contoh penggunaan tag `<title>`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Judul Halaman Web Anda</title>
</head>
<body>
  <!-- Konten halaman web -->
</body>
</html>
```

Pastikan untuk menggantikan "Judul Halaman Web Anda" dengan judul yang sesuai dengan halaman web Anda. Judul ini akan ditampilkan di bilah judul atau tab browser dan membantu pengguna mengidentifikasi konten halaman web.

Penting untuk menulis judul yang relevan, deskriptif, dan singkat. Judul yang baik akan membantu mesin pencari memahami topik halaman web Anda dan meningkatkan SEO (Search Engine Optimization) situs Anda.

Setelah menambahkan tag `<title>` dengan judul yang sesuai, simpan file HTML Anda dan buka di browser web. Anda akan melihat judul halaman Anda ditampilkan di bilah judul atau tab browser.

---
## Membuat Paragraf dengan tag p
Tag `<p>` digunakan untuk membuat paragraf atau blok teks dalam dokumen HTML. Paragraf biasanya digunakan untuk menyajikan teks yang terdiri dari beberapa kalimat yang terkait. Berikut adalah langkah-langkah untuk membuat paragraf menggunakan tag `<p>`:

1. Buka tag `<body>` dalam dokumen HTML Anda.
2. Di dalam tag `<body>`, tambahkan tag `<p>`.
3. Tulis teks paragraf Anda antara tag pembuka `<p>` dan penutup `</p>`.
4. Ulangi langkah 2 dan 3 untuk membuat paragraf tambahan jika diperlukan.
5. Setiap paragraf akan ditampilkan sebagai blok teks terpisah di halaman web.

Contoh penggunaan tag `<p>`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Judul Halaman Web Anda</title>
</head>
<body>
  <p>Ini adalah paragraf pertama.</p>
  <p>Ini adalah paragraf kedua.</p>
</body>
</html>
```

Dalam contoh di atas, kita membuat dua paragraf. Setiap paragraf ditempatkan di antara tag `<p>` dan `</p>`. Pada saat halaman web ditampilkan di browser, setiap paragraf akan ditampilkan sebagai blok teks terpisah dengan jarak antara satu paragraf dengan paragraf lainnya.

Anda dapat menulis teks apa pun di dalam tag `<p>`, seperti deskripsi, penjelasan, atau konten teks lainnya yang sesuai dengan halaman web Anda. Pastikan untuk menggunakan tag `<p>` untuk memisahkan setiap paragraf dan membuat teks terlihat terstruktur dan mudah dibaca oleh pengguna.

---
## Membuat Heading dengan tag h1 hinggan h6
Heading adalah elemen HTML yang digunakan untuk memberi judul pada konten atau teks tertentu. HTML menyediakan enam tingkatan heading yang disebut h1, h2, h3, h4, h5, dan h6.

Setiap tingkatan memiliki ukuran dan tingkat penting yang berbeda. Heading h1 biasanya digunakan untuk judul halaman, sedangkan h2 digunakan untuk sub-judul dan seterusnya.

Contoh penggunaan tag h1 hingga h6:

```
<!DOCTYPE html>
<html>
<head>
	<title>Contoh Heading HTML</title>
</head>
<body>
	<h1>Ini adalah heading h1</h1>
	<h2>Ini adalah heading h2</h2>
	<h3>Ini adalah heading h3</h3>
	<h4>Ini adalah heading h4</h4>
	<h5>Ini adalah heading h5</h5>
	<h6>Ini adalah heading h6</h6>
</body>
</html>
```

Pada contoh di atas, terdapat penggunaan tag h1 hingga h6 untuk membuat heading dengan tingkatan yang berbeda. Anda dapat mengganti teks pada masing-masing heading sesuai dengan kebutuhan Anda.

---
## Membuat tautan dengan tag a
Tag `<a>` (anchor) digunakan untuk membuat tautan atau link ke halaman web lain, file, atau bagian dalam halaman yang sama. Ketika pengguna mengklik tautan tersebut, mereka akan diarahkan ke URL atau bagian yang ditentukan. Berikut adalah langkah-langkah untuk membuat tautan menggunakan tag `<a>`:

1. Buka tag `<body>` dalam dokumen HTML Anda.
2. Di dalam tag `<body>`, tambahkan tag `<a>`.
3. Gunakan atribut `href` dalam tag `<a>` untuk menentukan URL atau tujuan tautan.
4. Tulis teks tautan Anda antara tag pembuka `<a>` dan penutup `</a>`.
5. Simpan tag `<a>` dalam konteks yang sesuai, seperti dalam paragraf atau elemen lainnya.

Contoh penggunaan tag `<a>`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Judul Halaman Web Anda</title>
</head>
<body>
  <p>Ini adalah <a href="https://www.example.com">tautan</a> ke situs web eksternal.</p>
  <p>Ini adalah <a href="page.html">tautan</a> ke halaman lain di situs web ini.</p>
  <p>Ini adalah <a href="#section">tautan</a> ke bagian dalam halaman yang sama.</p>
</body>
</html>
```

Dalam contoh di atas, kita membuat tiga tautan dengan menggunakan tag `<a>`. Tautan pertama mengarahkan pengguna ke situs web eksternal dengan URL `https://www.example.com`. Tautan kedua mengarahkan pengguna ke halaman lain dalam situs web dengan URL `page.html`. Tautan ketiga menggunakan atribut `href` dengan nilai `#section` untuk mengarahkan pengguna ke bagian dengan ID "section" dalam halaman yang sama.

Anda dapat mengganti nilai atribut `href` sesuai dengan tujuan tautan yang Anda inginkan. Pastikan untuk memberikan teks yang menjelaskan tujuan tautan di antara tag pembuka dan penutup `<a>`. Dengan menggunakan tag `<a>`, Anda dapat membuat navigasi antara halaman, menu, tautan ke konten terkait, dan banyak lagi dalam halaman web Anda.

---
# Mengelompokan dan Mengatur Konten
Dalam HTML, kita dapat menggunakan beberapa elemen untuk mengelompokkan dan mengatur konten dengan cara yang terstruktur. Beberapa elemen yang umum digunakan untuk tujuan ini adalah:

1. Tag `<div>`: Tag `<div>` digunakan untuk mengelompokkan elemen-elemen HTML ke dalam sebuah blok. Ini membantu dalam mengatur tata letak halaman dan memberikan gaya dengan menggunakan CSS. Anda dapat memberikan kelas atau ID pada elemen `<div>` untuk mengidentifikasinya secara unik.

2. Tag `<span>`: Tag `<span>` digunakan untuk mengelompokkan elemen HTML dalam blok kecil atau bagian kecil dari teks. Ini berguna ketika Anda ingin memberikan gaya atau memanipulasi bagian-bagian tertentu dari teks di dalam elemen yang lebih besar.

3. Tag `<section>`: Tag `<section>` digunakan untuk mengelompokkan konten terkait menjadi sebuah bagian dalam halaman. Ini membantu dalam mengorganisir dan mengidentifikasi bagian-bagian yang berbeda dalam konten halaman.

4. Tag `<article>`: Tag `<article>` digunakan untuk mengelompokkan konten yang merupakan entitas mandiri dan dapat berdiri sendiri. Misalnya, dalam blog, setiap postingan blog dapat dikelompokkan dalam elemen `<article>`.

5. Tag `<header>`: Tag `<header>` digunakan untuk mengelompokkan elemen-elemen yang berhubungan dengan bagian kepala (header) halaman, seperti judul, logo, navigasi, atau elemen penting lainnya.

6. Tag `<nav>`: Tag `<nav>` digunakan untuk mengelompokkan tautan navigasi ke bagian-bagian terkait halaman atau situs web.

7. Tag `<footer>`: Tag `<footer>` digunakan untuk mengelompokkan elemen-elemen yang terkait dengan bagian bawah halaman, seperti informasi hak cipta, tautan terkait, atau kredit.

Dengan menggunakan elemen-elemen ini, Anda dapat membagi dan mengatur konten halaman web dengan lebih terstruktur dan membuatnya lebih mudah dipahami oleh pengguna maupun oleh mesin pencari. Selain itu, Anda juga dapat memberikan gaya dan tata letak yang lebih baik dengan menggunakan CSS untuk elemen-elemen ini.

---
## Menggunakan tag div untuk membuat blok konten
Tag `<div>` adalah salah satu elemen paling umum dalam HTML yang digunakan untuk membuat blok konten di dalam halaman web. Ini tidak memberikan makna khusus pada konten yang dikandungnya, tetapi berfungsi sebagai wadah kosong yang dapat digunakan untuk mengelompokkan dan mengatur elemen-elemen HTML.

Berikut adalah langkah-langkah untuk menggunakan tag `<div>`:

1. Buka tag `<body>` dalam dokumen HTML Anda.
2. Di dalam tag `<body>`, tambahkan tag `<div>`.
3. Anda dapat menambahkan atribut seperti `class` atau `id` ke dalam tag `<div>` untuk memberikan identifikasi atau styling khusus.
4. Masukkan elemen-elemen HTML lainnya di dalam tag `<div>`.
5. Tutup tag `<div>` dengan menambahkan tag penutup `</div>`.

Contoh penggunaan tag `<div>`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Judul Halaman Web Anda</title>
</head>
<body>
  <div>
    <h1>Judul Konten</h1>
    <p>Ini adalah paragraf pertama.</p>
    <p>Ini adalah paragraf kedua.</p>
    <img src="gambar.jpg" alt="Gambar">
  </div>
</body>
</html>
```

Dalam contoh di atas, kami menggunakan tag `<div>` untuk membuat blok konten yang mengelompokkan elemen-elemen HTML lainnya. Konten yang dikandung oleh tag `<div>` meliputi sebuah judul (`<h1>`), dua paragraf (`<p>`), dan sebuah gambar (`<img>`). Anda dapat menggunakan CSS untuk memberikan gaya, tata letak, atau manipulasi lainnya pada blok konten ini.

Tag `<div>` sangat berguna dalam mengatur tata letak dan struktur halaman web. Anda dapat membuat beberapa blok konten menggunakan tag `<div>` dan memberikan kelas atau ID yang berbeda untuk mengidentifikasinya. Ini memungkinkan Anda untuk mengaplikasikan gaya atau manipulasi yang berbeda pada setiap blok konten tersebut.

---
## Menggunakan tag span untuk menandai bagian kecil dari teks
Tag `<span>` digunakan untuk menandai bagian kecil dari teks di dalam elemen yang lebih besar. Perbedaannya dengan tag `<div>` adalah tag `<span>` tidak membuat perubahan tampilan secara langsung tanpa adanya CSS. Sebagai contoh, Anda dapat menggunakan tag `<span>` untuk menandai bagian kata yang ingin diberikan penekanan atau perubahan styling tertentu. Berikut adalah contoh penggunaan tag `<span>`:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Judul Halaman Web Anda</title>
</head>
<body>
  <h1>Ini adalah <span>judul</span> halaman web</h1>
  <p>Ini adalah <span>paragraf pertama</span> dan ini adalah <span>paragraf kedua</span>.</p>
</body>
</html>
```

Dalam contoh di atas, kita menggunakan tag `<span>` untuk menandai bagian kata yang ingin diberikan penekanan. Misalnya, kata "judul" dalam judul halaman dan "paragraf pertama" serta "paragraf kedua" dalam paragraf. Tanpa adanya CSS, secara langsung tidak ada perubahan tampilan yang terjadi. Namun, tag `<span>` memberikan fleksibilitas saat digunakan bersama dengan CSS, di mana Anda dapat memberikan gaya dan manipulasi tertentu pada bagian yang ditandai oleh tag `<span>`.

Berikut adalah contoh penggunaan tag `<span>` dengan CSS untuk memberikan gaya pada bagian teks yang ditandai:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Judul Halaman Web Anda</title>
  <style>
    .highlight {
      color: red;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Ini adalah <span class="highlight">judul</span> halaman web</h1>
  <p>Ini adalah <span class="highlight">paragraf pertama</span> dan ini adalah <span class="highlight">paragraf kedua</span>.</p>
</body>
</html>
```

Dalam contoh di atas, kita telah menambahkan blok `<style>` di dalam elemen `<head>` untuk menentukan gaya menggunakan CSS. Di dalam blok tersebut, kita memberikan gaya pada kelas `.highlight` yang diberikan pada tag `<span>`.

CSS yang diberikan dalam contoh tersebut memberikan teks yang ditandai oleh `<span class="highlight">` menjadi berwarna merah dan diberi penekanan tebal. Anda dapat mengubah properti CSS sesuai dengan preferensi Anda untuk memberikan gaya yang diinginkan.

Dengan menggunakan CSS, tag `<span>` dapat digunakan untuk memberikan gaya pada bagian teks tertentu dalam elemen yang lebih besar. Ini memberikan fleksibilitas dalam mendesain dan menyoroti bagian-bagian penting dari teks di dalam halaman web Anda.

---
## Membuat daftar dengan tag ul, ol, dan li
Oke, jadi dalam HTML kita bisa membuat daftar dengan menggunakan tag `<ul>`, `<ol>`, dan `<li>`. `<ul>` digunakan untuk membuat daftar dengan bullet (poin), sedangkan `<ol>` digunakan untuk membuat daftar dengan angka atau huruf sebagai penomoran. Sedangkan `<li>` digunakan untuk menandai setiap elemen dalam daftar.

Contoh penggunaannya seperti ini:
```html
<ul>
  <li>Buah jeruk</li>
  <li>Buah apel</li>
  <li>Buah mangga</li>
</ul>

<ol>
  <li>Buah jeruk</li>
  <li>Buah apel</li>
  <li>Buah mangga</li>
</ol>
```

Dalam contoh di atas, kita membuat daftar buah menggunakan `<ul>` dan `<ol>`. Setiap elemen dalam daftar ditandai dengan tag `<li>`.

Hasilnya akan terlihat seperti ini:
- Buah jeruk
- Buah apel
- Buah mangga

1. Buah jeruk
2. Buah apel
3. Buah mangga

---
## Membuat tabel dengan tag table, tr, th, dan td
Tentu! Dalam HTML, kita dapat membuat tabel menggunakan tag `<table>`, `<tr>`, `<th>`, dan `<td>`. Berikut adalah penjelasan tentang masing-masing tag tersebut:

- `<table>`: Tag ini digunakan untuk membuat sebuah tabel di dalam dokumen HTML.
- `<tr>`: Tag ini digunakan untuk membuat sebuah baris (row) dalam tabel.
- `<th>`: Tag ini digunakan untuk membuat sel header dalam tabel. Biasanya digunakan di dalam baris pertama (atau baris header) untuk menandai judul kolom.
- `<td>`: Tag ini digunakan untuk membuat sel data dalam tabel. Digunakan di dalam baris (row) untuk menandai data dalam kolom tersebut.

Contoh penggunaannya sebagai berikut:

```html
<table>
  <tr>
    <th>Nama</th>
    <th>Umur</th>
    <th>Kota</th>
  </tr>
  <tr>
    <td>John</td>
    <td>25</td>
    <td>New York</td>
  </tr>
  <tr>
    <td>Lisa</td>
    <td>30</td>
    <td>London</td>
  </tr>
</table>
```

Dalam contoh di atas, kita membuat tabel dengan tiga kolom: Nama, Umur, dan Kota. Baris pertama merupakan baris header yang ditandai dengan tag `<th>`, sedangkan baris-baris berikutnya merupakan data yang ditandai dengan tag `<td>`.

Hasilnya akan terlihat seperti ini:

```
| Nama  | Umur | Kota    |
|-------|------|---------|
| John  | 25   | New York|
| Lisa  | 30   | London  |
```

Tabel digunakan untuk menyusun dan menampilkan data secara terstruktur di dalam halaman web. Dengan menggunakan kombinasi tag `<table>`, `<tr>`, `<th>`, dan `<td>`, kita dapat dengan mudah membuat tabel yang rapi dan informatif.

---
# Menampilkan Gambar dan Media
Dalam HTML, kita dapat menampilkan gambar dan media dengan menggunakan beberapa tag. Berikut adalah penjelasan singkat tentang menampilkan gambar dan media dalam HTML:

1. `<img>`: Tag ini digunakan untuk menampilkan gambar di halaman web. Kita dapat menentukan sumber gambar menggunakan atribut `src` dan memberikan deskripsi alternatif menggunakan atribut `alt`.

2. `<video>`: Tag ini digunakan untuk menampilkan video di halaman web. Kita dapat menentukan sumber video menggunakan atribut `src` dan mengatur pengaturan video lainnya menggunakan atribut-atribut seperti `controls` (untuk menampilkan kontrol pemutaran), `autoplay` (untuk memulai pemutaran secara otomatis), dan lainnya.

3. `<audio>`: Tag ini digunakan untuk menampilkan audio di halaman web. Kita dapat menentukan sumber audio menggunakan atribut `src` dan mengatur pengaturan audio lainnya menggunakan atribut-atribut seperti `controls` (untuk menampilkan kontrol pemutaran), `autoplay` (untuk memulai pemutaran secara otomatis), dan lainnya.

4. `<iframe>`: Tag ini digunakan untuk menampilkan konten lain dari halaman web lain di dalam halaman web saat ini. Kita dapat menentukan sumber halaman web menggunakan atribut `src` dan mengatur ukuran dan atribut lainnya.

5. `<figure>` dan `<figcaption>`: Tag `<figure>` digunakan untuk mengelompokkan konten media seperti gambar atau video bersama dengan deskripsi atau caption yang terkait. Tag `<figcaption>` digunakan untuk menambahkan deskripsi atau caption untuk elemen media di dalam tag `<figure>`.

Dengan menggunakan tag-tag ini, kita dapat dengan mudah menampilkan gambar, video, audio, dan konten media lainnya di halaman web.

---
## Menambahkan gambar dengan tag img
Dalam HTML, kita dapat menambahkan gambar ke halaman web menggunakan tag `<img>`. Berikut adalah penjelasan singkat tentang penggunaan tag `<img>`:

- `<img>`: Tag ini digunakan untuk menampilkan gambar di halaman web. Kita dapat menentukan sumber gambar menggunakan atribut `src` yang berisi URL atau path ke gambar.

Contoh penggunaannya sebagai berikut:

```html
<img src="path_ke_gambar/gambar.jpg" alt="Deskripsi Gambar">
```

Dalam contoh di atas, kita menggunakan tag `<img>` untuk menampilkan gambar. Atribut `src` digunakan untuk menentukan sumber gambar dengan menyertakan URL atau path ke gambar. Atribut `alt` digunakan untuk memberikan deskripsi alternatif tentang gambar, yang akan ditampilkan jika gambar tidak dapat dimuat atau jika pengguna menggunakan pembaca layar.

Pastikan untuk menggantikan `path_ke_gambar/gambar.jpg` dengan URL atau path yang sesuai dengan lokasi gambar di dalam proyek Anda. Gunakan deskripsi yang relevan untuk atribut `alt`, sehingga pengguna dengan masalah aksesibilitas atau jika gambar tidak dapat dimuat masih dapat memahami konten gambar.

Menggunakan tag `<img>`, kita dapat menampilkan gambar di halaman web dengan mudah. Selain itu, tag ini juga memiliki atribut tambahan seperti `width` dan `height` untuk mengatur ukuran gambar, serta atribut lainnya untuk pengaturan lebih lanjut.

---
## Menambahkan video dengan tag video
Oke! Dalam HTML, kita dapat menambahkan video ke halaman web menggunakan tag `<video>`. Berikut adalah penjelasan singkat tentang penggunaan tag `<video>`:

- `<video>`: Tag ini digunakan untuk menampilkan video di halaman web. Kita dapat menentukan sumber video menggunakan atribut `src` yang berisi URL atau path ke video.

Contoh penggunaannya sebagai berikut:

```html
<video src="path_ke_video/video.mp4" controls></video>
```

Dalam contoh di atas, kita menggunakan tag `<video>` untuk menampilkan video. Atribut `src` digunakan untuk menentukan sumber video dengan menyertakan URL atau path ke video. Atribut `controls` digunakan untuk menampilkan kontrol pemutaran video seperti pemutaran, jeda, dan pengaturan volume.

Pastikan untuk menggantikan `path_ke_video/video.mp4` dengan URL atau path yang sesuai dengan lokasi video di dalam proyek Anda.

Tag `<video>` juga memiliki atribut tambahan seperti `autoplay` (untuk memulai pemutaran video secara otomatis), `loop` (untuk mengulangi video setelah selesai), dan atribut lainnya untuk pengaturan lebih lanjut.

Dengan menggunakan tag `<video>`, kita dapat menampilkan video di halaman web dengan mudah dan memberikan kontrol pemutaran kepada pengguna.

---
## Menambahkan audio dengan tag audio
Dalam HTML, kita dapat menambahkan audio ke halaman web menggunakan tag `<audio>`. Berikut adalah penjelasan singkat tentang penggunaan tag `<audio>`:

- `<audio>`: Tag ini digunakan untuk memasukkan audio ke halaman web. Kita dapat menentukan sumber audio menggunakan atribut `src` yang berisi URL atau path ke file audio.

Contoh penggunaannya sebagai berikut:

```html
<audio src="path_ke_audio/audio.mp3" controls></audio>
```

Dalam contoh di atas, kita menggunakan tag `<audio>` untuk menampilkan audio. Atribut `src` digunakan untuk menentukan sumber audio dengan menyertakan URL atau path ke file audio. Atribut `controls` digunakan untuk menampilkan kontrol pemutaran audio seperti pemutaran, jeda, dan pengaturan volume.

Pastikan untuk menggantikan `path_ke_audio/audio.mp3` dengan URL atau path yang sesuai dengan lokasi file audio di dalam proyek Anda.

Tag `<audio>` juga memiliki atribut tambahan seperti `autoplay` (untuk memulai pemutaran audio secara otomatis), `loop` (untuk mengulangi audio setelah selesai), dan atribut lainnya untuk pengaturan lebih lanjut.

Dengan menggunakan tag `<audio>`, kita dapat menyisipkan audio ke halaman web dengan mudah dan memberikan kontrol pemutaran kepada pengguna.

---
## Menambahkan konten lain dengan tag iframe
Dalam HTML, kita dapat menambahkan konten dari sumber eksternal ke halaman web menggunakan tag `<iframe>`. Berikut adalah penjelasan singkat tentang penggunaan tag `<iframe>`:

- `<iframe>`: Tag ini digunakan untuk menyisipkan konten dari sumber eksternal ke halaman web. Konten ini bisa berupa halaman web lain, video, peta, atau elemen interaktif lainnya.

Contoh penggunaannya sebagai berikut:

```html
<iframe src="https://www.youtube.com/embed/video_id"></iframe>
```

Dalam contoh di atas, kita menggunakan tag `<iframe>` untuk menyisipkan konten dari YouTube. Atribut `src` digunakan untuk menentukan sumber konten eksternal dengan menyertakan URL lengkap ke sumber tersebut.

Pastikan untuk menggantikan `https://www.youtube.com/embed/video_id` dengan URL yang sesuai dengan konten eksternal yang ingin Anda sisipkan.

Selain atribut `src`, tag `<iframe>` juga memiliki atribut lain seperti `width` dan `height` untuk mengatur lebar dan tinggi iframe, serta atribut lainnya untuk pengaturan lebih lanjut.

Dengan menggunakan tag `<iframe>`, kita dapat menyisipkan konten dari sumber eksternal ke halaman web dengan mudah dan memberikan pengalaman yang lebih interaktif bagi pengguna.

---
## Menggunakan tag figure dan figcaption
Dalam HTML, kita dapat menggunakan tag `<figure>` dan `<figcaption>` untuk mengelompokkan gambar atau media dengan keterangan terkait. Berikut adalah penjelasan singkat tentang penggunaan tag `<figure>` dan `<figcaption>`:

- `<figure>`: Tag ini digunakan untuk mengelompokkan konten gambar atau media dengan keterangan terkait. Biasanya, tag `<figure>` digunakan untuk menampilkan gambar, ilustrasi, diagram, atau elemen media lainnya.

- `<figcaption>`: Tag ini digunakan untuk memberikan keterangan atau deskripsi terkait dengan gambar atau media yang terkandung dalam tag `<figure>`. Biasanya, tag `<figcaption>` ditempatkan di dalam tag `<figure>` dan berfungsi sebagai judul atau penjelasan dari konten yang ditampilkan.

Contoh penggunaannya sebagai berikut:

```html
<figure>
  <img src="path_ke_gambar/gambar.jpg" alt="Deskripsi Gambar">
  <figcaption>Keterangan Gambar</figcaption>
</figure>
```

Dalam contoh di atas, kita menggunakan tag `<figure>` untuk mengelompokkan gambar dengan keterangan terkait. Gambar ditampilkan menggunakan tag `<img>` dengan atribut `src` yang menentukan sumber gambar dan atribut `alt` yang memberikan deskripsi alternatif untuk aksesibilitas. Keterangan gambar ditempatkan di dalam tag `<figcaption>`.

Pastikan untuk menggantikan `path_ke_gambar/gambar.jpg` dengan URL atau path yang sesuai dengan lokasi gambar di dalam proyek Anda.

Dengan menggunakan tag `<figure>` dan `<figcaption>`, kita dapat mengelompokkan gambar atau media dengan keterangan terkait, sehingga memudahkan pembaca untuk memahami konteks atau informasi yang disampaikan.

---
# Membuat Formulir
Formulir dalam HTML adalah elemen yang digunakan untuk mengumpulkan data dari pengguna melalui halaman web. Formulir memberikan pengguna antarmuka untuk memasukkan informasi, seperti nama, alamat email, komentar, pilihan, dan sebagainya. Data yang dimasukkan oleh pengguna kemudian dapat dikirim ke server untuk diproses lebih lanjut.

Formulir biasanya terdiri dari beberapa elemen seperti bidang masukan (input fields), area teks, menu dropdown, tombol, dan lain-lain. Elemen-elemen ini ditandai dengan tag HTML khusus seperti `<input>`, `<textarea>`, `<select>`, dan sebagainya. Tag `<form>` digunakan untuk mengelompokkan elemen-elemen ini menjadi satu kesatuan.

Setiap elemen formulir memiliki atribut yang penting. Beberapa atribut yang umum digunakan adalah:

- `name`: Menentukan nama unik untuk elemen formulir. Nama ini akan digunakan untuk mengidentifikasi nilai yang dikirimkan ke server.
- `type`: Digunakan untuk elemen `<input>`, menentukan jenis bidang masukan yang ingin digunakan, seperti teks, email, password, checkbox, radio button, dan lain-lain.
- `value`: Menentukan nilai default untuk elemen formulir.
- `placeholder`: Memberikan teks petunjuk yang ditampilkan di dalam elemen formulir, memberikan panduan kepada pengguna tentang apa yang diharapkan.
- `required`: Digunakan untuk membuat suatu elemen formulir menjadi wajib diisi sebelum data formulir dapat dikirimkan.
- `action`: Menentukan URL atau skrip yang akan memproses data formulir.
- `method`: Menentukan metode pengiriman data formulir ke server, seperti `post` (data dikirimkan dalam permintaan terpisah) atau `get` (data ditambahkan ke URL).

Dengan menggunakan tag-tag dan atribut-atribut tersebut, Anda dapat membuat formulir yang memenuhi kebutuhan Anda dan mengumpulkan data dari pengguna. Data yang dikirimkan ke server dapat digunakan untuk berbagai macam tujuan, seperti menyimpan data pengguna, mengirim email, melakukan validasi, dan lain-lain.

---
## Menggunakan tag form untuk membuat formulir
Tag `<form>` digunakan untuk membuat area formulir di halaman web. Contoh penggunaan tag `<form>`:
```html
<form action="/proses-data" method="post">
    <!-- Konten formulir -->
</form>
```
Dalam contoh di atas, `<form>` digunakan untuk mengelompokkan elemen-elemen formulir. Atribut `action` menentukan URL atau skrip yang akan memproses data formulir. Atribut `method` menentukan metode pengiriman data formulir ke server (misalnya, `post` atau `get`).

---
## Menambahkan bidang masukan dengan tag input
Menambahkan bidang masukan dengan tag `<input>`:
Tag `<input>` digunakan untuk membuat bidang masukan seperti teks, email, password, checkbox, dan sebagainya. Contoh penggunaan tag `<input>`:
```html
<input type="text" name="nama" placeholder="Masukkan nama Anda">
```
Dalam contoh di atas, `<input>` digunakan untuk membuat bidang masukan teks dengan atribut `type="text"`. Atribut `name` digunakan untuk memberikan nama unik untuk bidang masukan. Atribut `placeholder` memberikan teks petunjuk di dalam bidang masukan.

---
## Menggunakan tag textarea untuk memasukkan teks panjang
Tag `<textarea>` digunakan untuk membuat area teks yang lebih panjang, seperti untuk komentar atau pesan. Contoh penggunaan tag `<textarea>`:
```html
<textarea name="pesan" placeholder="Tulis pesan Anda"></textarea>
```
Dalam contoh di atas, `<textarea>` digunakan untuk membuat area teks panjang dengan atribut `name` untuk memberikan nama dan atribut `placeholder` untuk teks petunjuk.

---
## Menggunakan tag select dan option untuk membuat menu dropdown.
Tag `<select>` dan `<option>` digunakan untuk membuat menu dropdown atau pilihan. Contoh penggunaan tag `<select>` dan `<option>`:
```html
<select name="jenis-kelamin">
    <option value="pria">Pria</option>
    <option value="wanita">Wanita</option>
</select>
```
Dalam contoh di atas, `<select>` digunakan untuk membuat menu dropdown dengan atribut `name` untuk memberikan nama. Tag `<option>` digunakan untuk menambahkan opsi dalam menu dropdown. Nilai `value` dalam tag `<option>` akan dikirimkan ke server saat formulir dikirimkan.

Dengan memahami konsep tersebut, Anda dapat membuat formulir yang berisi bidang masukan, area teks, dan menu dropdown. Selanjutnya, Anda dapat mengirimkan data formulir ke server untuk diproses sesuai dengan URL atau skrip yang ditentukan dalam atribut `action` pada tag `<form>`.

---
# Penutup
Selamat! Kamu telah berhasil menjelajahi dunia HTML bersama kita. Sekarang saatnya untuk membuka bab baru dalam petualanganmu dan menjelajahi CSS. Jadi, apa itu CSS? Nah, CSS itu seperti senjata rahasia yang akan membuat tampilan halaman webmu terlihat super keren dan stylish.

Dengan CSS, kamu dapat memberikan gaya dan kehidupan pada elemen-elemen HTML-mu. Kamu bisa mengubah warna, menyesuaikan tata letak, membuat efek animasi, dan masih banyak lagi. Dalam waktu singkat, kamu akan menjadi seorang ninja CSS yang mampu menciptakan tampilan web yang memukau.

Jadi, jangan berhenti di sini! Mari kita melanjutkan petualangan ini dengan mempelajari semua trik dan trik CSS yang akan membantu mengubah halaman web-mu menjadi karya seni digital. Bersiaplah untuk menjadi seorang desainer web yang keren dan tak terkalahkan!

Terima kasih telah bergabung dengan kami dalam pembahasan HTML. Selamat belajar tentang CSS dan bersiaplah untuk menciptakan situs web yang "wow"! Teruslah berkreasi dan jangan takut mencoba hal-hal baru. Kami sangat bersemangat untuk melihat apa yang akan kamu ciptakan selanjutnya. Sampai jumpa di dunia CSS!

---