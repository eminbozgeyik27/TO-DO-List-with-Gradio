# 📝 To Do List with Gradio

Bu proje, **Gradio** ve **SQLite** kullanarak geliştirilmiş kullanıcı tabanlı bir **To Do List (Yapılacaklar Listesi)** uygulamasıdır. Kullanıcılar kayıt olabilir, giriş yapabilir, görev ekleyebilir, silebilir, düzenleyebilir ve görev listesini görüntüleyebilir.

---

## 🌟 Özellikler

- ✅ Kullanıcı **kayıt** ve **giriş** işlemleri  
- ✅ Görev **ekleme**, **silme** ve **düzenleme**  
- ✅ Kullanıcıya özel görev listesi  
- ✅ Görevleri **yenileme** ve anlık görüntüleme  
- ✅ **Çıkış** yapabilme  

---

## 💻 Gereksinimler

- Python 3.8 veya üzeri  
- [Gradio](https://gradio.app/)  
- SQLite (Python ile birlikte gelir)  

Kurulum için gerekli paket:  
```bash
pip install gradio
```

---

## 🚀 Kurulum ve Çalıştırma

1. Repository’yi klonlayın veya indirin:

```bash
git clone https://github.com/eminbozgeyik27/TO-DO-List-with-Gradio.git
cd TO-DO-List-with-Gradio
```

2. Veritabanını oluşturup uygulamayı başlatın:

```bash
python app.py
```

> Not: Dosya adınız farklıysa kendi dosya adınızı kullanın.  

3. Tarayıcıda açılan Gradio arayüzünden uygulamayı kullanabilirsiniz.

---

## 🛠️ Kullanım Adımları

### 1️⃣ Kayıt Tabı
Yeni kullanıcı oluşturun:  
- Kullanıcı adı ve şifre girin  
- “Kayıt Ol” butonuna tıklayın  

### 2️⃣ Giriş Tabı
Mevcut kullanıcı ile giriş yapın:  
- Kullanıcı adı ve şifre girin  
- “Giriş Yap” butonuna tıklayın  

### 3️⃣ To Do List Tabı
- Yeni görev ekleyin  
- Görevleri listeleyin ve yenileyin  

### 4️⃣ Görev Sil Tabı
- Silmek istediğiniz görevi girin  
- “Görev Sil” butonuna tıklayın  

### 5️⃣ Görev Düzenle Tabı
- Düzenlenecek görevi girin  
- Yeni görevi yazın  
- “Görev Düzenle” butonuna tıklayın  

### 6️⃣ Çıkış Tabı
- Kullanıcıdan çıkış yapın  

---

## 🗄️ Veritabanı Yapısı

- **Veritabanı Dosyası**: `kullanicilar.db`  
- **Tablolar**:  
1. `kullanicilar` – Kullanıcı adı ve şifre  
2. `kullanici_portfoyu` – Kullanıcıya ait görevler  

---

## 📌 Örnek Kullanım

**Yeni Görev Ekleme:**  
```
Görev: Alışveriş Yap
Sonuç: 'Alışveriş Yap' görevine eklendi.
Güncel Görevler:
- Alışveriş Yap
```

**Görev Silme:**  
```
Görev: Alışveriş Yap
Sonuç: 'Alışveriş Yap' görevi silindi.
```

---

## 🖼️ Görselli Arayüz

Gradio sayesinde tüm işlemler **web tabanlı ve görsel bir arayüz** üzerinden yapılabilir.  
- Kayıt ve giriş penceresi  
- Görev ekleme, silme ve düzenleme alanları  
- Görev listesini anlık görüntüleme butonları  

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.
