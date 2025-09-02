import gradio as gr
import sqlite3



DB_PATH = "kullanicilar.db"


def db():

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS kullanicilar (name TEXT PRIMARY KEY, password TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS kullanici_portfoyu (name TEXT, todo TEXT, date TEXT)")

    con.commit()
    con.close()


def kayit(name, password):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    try:
        if name == "" or password == "":
            return "Kullanıcı adı ve şifre boş olamaz."
        cur.execute("INSERT INTO kullanicilar (name, password) VALUES (?, ?)", (name, password))
        con.commit()
        return "Kayıt başarıyla tamamlandı!"
    except sqlite3.IntegrityError:
        return "Bu kullanıcı adı zaten kayıtlı."
    finally:
        con.close()


def giris(name, password):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT * FROM kullanicilar WHERE name=? AND password=?", (name, password))
    user = cur.fetchone()
    con.close()
    if user:
        return True, f"Giriş başarılı! Hoşgeldin {name}"
    else:
        return False, "Kullanıcı adı veya şifre yanlış!"


def add_todo(name, todo):
    if not todo:
        return "Lütfen görev giriniz."

    todos = list_todos(name)
    if todo in todos:
        return "Görevler aynı olamaz."


    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("INSERT INTO kullanici_portfoyu (name, todo ,date) VALUES (?, ?, ?)", (name, todo, add_date_todo))
    con.commit()
    con.close()
    return f"'{todo}' görevine eklendi."


def list_todos(name):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT todo, date FROM kullanici_portfoyu WHERE name=?", (name,))
    todos = cur.fetchall()
    con.close()
    if not todos:
        return "Henüz görev yok."
    return "\n".join(f"{t[0]} - {t[1]}" for t in todos)


def add_date(tarih):
    global add_date_todo
    add_date_todo = tarih

def update_date(tarih):
    global update_date_todo
    update_date_todo = tarih










db()

with gr.Blocks() as todo_app:
    state = gr.State()

    with gr.Tabs():
        with gr.TabItem("Kayıt"):
            kayit_name = gr.Textbox(label="Kullanıcı Adı")
            kayit_pass = gr.Textbox(label="Şifre", type="password")
            kayit_output = gr.Textbox(label="Sonuç")
            kayit_btn = gr.Button("Kayıt Ol")
            kayit_btn.click(kayit, inputs=[kayit_name, kayit_pass], outputs=kayit_output)

        with gr.TabItem("Giriş"):
            giris_name = gr.Textbox(label="Kullanıcı Adı")
            giris_pass = gr.Textbox(label="Şifre", type="password")
            giris_output = gr.Textbox(label="Sonuç")
            giris_btn = gr.Button("Giriş Yap")


            def login_and_set_state(name, password):
                success, msg = giris(name, password)
                if success:
                    return msg, name
                else:
                    return msg, None


            giris_btn.click(fn=login_and_set_state, inputs=[giris_name, giris_pass], outputs=[giris_output, state])

        with gr.TabItem("To Do List"):
            gr.Markdown("**To Do List Sayfası**")
            todo_input = gr.Textbox(label="Yeni Görev")
            todo_date = gr.DateTime(label="Tarih", type="string", include_time= True)
            todo_btn = gr.Button("Görev Ekle")
            todo_output = gr.Textbox(label="Görevler")


            def add_and_list(name, todo):
                if not name:
                    return "Lütfen önce giriş yapın."
                mesaj = add_todo(name, todo)
                liste = list_todos(name)

                return f"{mesaj}\n\nGüncel Görevler:\n{liste}"


            todo_btn.click(add_and_list, inputs=[state, todo_input], outputs=todo_output)
            todo_date.change(add_date, inputs=todo_date, outputs=todo_output)



            def show_todos(name):
                if not name:
                    return "Lütfen önce giriş yapın."
                return list_todos(name)

            refresh_btn = gr.Button("Görevleri Yenile")

            refresh_btn.click(show_todos, inputs=state, outputs=todo_output)





        with gr.TabItem("Görev Sil"):
            sil_todo = gr.Textbox(label="Silinecek Görev")
            sil_btn = gr.Button("Görev Sil")
            sil_output = gr.Textbox(label="Sonuç")

            def delete_todo(name, todo):
                if not name:
                    return "Lütfen önce giriş yapın."
                if not todo:
                    return "Lütfen silinecek görevi giriniz."
                if todo not in list_todos(name):
                    return f"'{todo}' görevi bulunamadı."
                con = sqlite3.connect(DB_PATH)
                cur = con.cursor()
                cur.execute("DELETE FROM kullanici_portfoyu WHERE name=? AND todo=?", (name, todo))
                con.commit()
                con.close()
                return f"'{todo}' görevi silindi."

            def show_todos_2(name):
                if not name:
                    return "Lütfen önce giriş yapın."
                return list_todos(name)

            refresh_btn = gr.Button("Görevleri Yenile")

            refresh_btn.click(show_todos_2, inputs=state, outputs=sil_output)

            sil_btn.click(delete_todo, inputs=[state, sil_todo], outputs=sil_output)

        with gr.TabItem("Görev Düzenle"):
            duzenle_todo = gr.Textbox(label="Düzenlenecek Görev")
            duzenle_yeni_todo = gr.Textbox(label="Yeni Görev")
            duzenle_tarih = gr.DateTime(label="Tarih", type="string", include_time=True)

            duzenle_btn = gr.Button("Görev Düzenle")

            duzenle_output = gr.Textbox(label="Sonuç")

            def update_todo(name, todo, yeni_todo):
                if not name:
                    return "Lütfen önce giriş yapın."
                if not todo:
                    return "Lütfen düzenlenecek görevi giriniz."
                if todo not in list_todos(name):
                    return f"'{todo}' görevi bulunamadı."
                if yeni_todo == "":
                    return "Lütfen yeni görevi giriniz."
                if todo == yeni_todo:
                    return "Görevler aynı olamaz."
                con = sqlite3.connect(DB_PATH)
                cur = con.cursor()

                cur.execute("UPDATE kullanici_portfoyu SET todo=?, date=? WHERE name=? AND todo=?", (yeni_todo, update_date_todo, name, todo))
                con.commit()
                con.close()
                return f"'{todo}' görevi düzenlendi."

            def show_todos_3(name):
                if not name:
                    return "Lütfen önce giriş yapın."
                return list_todos(name)

            refresh_btn = gr.Button("Görevleri Yenile")

            refresh_btn.click(show_todos_3, inputs=state, outputs=duzenle_output)
            duzenle_tarih.change(update_date, inputs=duzenle_tarih, outputs=duzenle_output)

            duzenle_btn.click(update_todo, inputs=[state, duzenle_todo, duzenle_yeni_todo], outputs=duzenle_output)



        with gr.TabItem("Çıkış"):
            cikis_btn = gr.Button("Çıkış Yap")
            cikis_output = gr.Textbox(label="Sonuç")
            def sign_out():
                msg = "Çıkıs Yapıldı."
                return msg, None
            cikis_btn.click(sign_out, outputs=[cikis_output, state])


todo_app.launch()
