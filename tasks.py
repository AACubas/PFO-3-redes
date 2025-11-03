from queue import Queue
import threading
import time
from db import get_connection

task_queue = Queue()

def analizar_texto(texto):
    """Simula un análisis de texto."""
    palabras = len(texto.split())
    longitud = len(texto)
    sentimiento = "positivo" if "feliz" in texto.lower() else "neutral"
    time.sleep(2)  # Simula un tiempo de procesamiento
    return f"{palabras} palabras, {longitud} caracteres, sentimiento: {sentimiento}"

def worker():
    """Worker que procesa textos pendientes."""
    while True:
        analisis_id, texto = task_queue.get()
        resultado = analizar_texto(texto)
        conn = get_connection()
        c = conn.cursor()
        c.execute("UPDATE analisis SET resultado=?, estado='completado' WHERE id=?", (resultado, analisis_id))
        conn.commit()
        conn.close()
        task_queue.task_done()

def start_workers(num_workers=3):
    for _ in range(num_workers):
        t = threading.Thread(target=worker, daemon=True)
        t.start()
