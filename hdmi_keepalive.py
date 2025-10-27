#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HDMI Keep Alive for Linux
-------------------------
Simule une activité sur la sortie HDMI/DP pour éviter que la TV change de source.
Compatible avec plusieurs écrans, totalement invisible.
"""

###
# penser a installer tk 
# sur arch: "sudo pacman -Sy tk"
# sur debian: "apt install python3-tk tk tk-dev libtcl8.6 libtk8.6 -y"
# creation du venv + "pip install screeninfo"
###

import os
import tkinter as tk
import time
import threading
import signal
import sys
import screeninfo

def check_environment():
    """Vérifier si nous sommes dans un virtualenv"""

    """if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print(f"✓ Virtualenv activé: {sys.prefix}")
    else:
        print("⚠ Aucun virtualenv détecté")
    
    print(f"Python exécutable: {sys.executable}")
    """
    venv_path = os.environ.get('VIRTUAL_ENV')
    if venv_path:
        print(f"✓ Virtualenv activé: {venv_path}")
    else:
        print("⚠ Aucun virtualenv détecté")
    
    print(f"💡 Python utilisé: {sys.executable}")


def find_hdmi_monitor():
    """Tente de détecter un écran HDMI à partir des infos EDID."""

    monitors = screeninfo.get_monitors()
    for m in monitors:
        # On cherche 'HDMI' dans le nom du moniteur ou son ID
        #if "HDMI" in m.name.upper() or "HDMI" in getattr(m, "device", "").upper():
        if ("HDMI" in m.name.upper() or "DP" in m.name.upper()) and not m.name.upper().startswith("EDP"):
            return m
    # Sinon, on retourne le deuxième écran s’il existe
    if len(monitors) > 1:
        return monitors[1]
    # Par défaut, on renvoie le principal
    return monitors[0]


def keep_hdmi_alive(canvas, DEBUG):
    """Change la couleur d’un pixel invisible pour simuler un rafraîchissement vidéo."""

    TOGGLE = False
    while True:
        color = "#000001" if TOGGLE else "#000000"
        canvas.create_rectangle(0, 0, 1, 1, fill=color, outline=color)
        canvas.update()
        TOGGLE = not TOGGLE
        time.sleep(30)
        if DEBUG:
            print("✅ Pixel maj")


def start_hdmi_simulator(DEBUG):
    """Crée une fenêtre invisible sur l’écran HDMI détecté."""

    monitor = find_hdmi_monitor()
    print(f"✅ Écran HDMI détecté : {monitor.name} ({monitor.width}x{monitor.height} @ {monitor.x},{monitor.y})")

    root = tk.Tk()
    root.title("HDMI Keep Alive")

    # Fenêtre totalement invisible
    root.overrideredirect(True)
    root.attributes("-alpha", 0.0)
    # Positionne sur l’écran HDMI détecté
    root.geometry(f"1x1+{monitor.x}+{monitor.y}")

    canvas = tk.Canvas(root, width=1, height=1, highlightthickness=0)
    canvas.pack()

    threading.Thread(target=keep_hdmi_alive, args=(canvas,DEBUG,), daemon=True).start()

    print("💡 Simulation HDMI active. Fermez la fenêtre ou Ctrl+C pour arrêter.")
    root.mainloop()


def signal_handler(sig, frame):
    """Intercepte Ctrl+C proprement."""

    print("\n⛔️ Simulation HDMI arrêtée proprement.")
    sys.exit(0)


if __name__ == "__main__":

    DEBUG=False

    check_environment()

    # Gestion du Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print("💡 Lancement de HDMI Keep Alive...")
    start_hdmi_simulator(DEBUG)
