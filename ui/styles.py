import customtkinter as ctk

def apply_modern_style():
    """Aplica el tema moderno a la aplicación"""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

def get_button_style():
    """Retorna estilo para botones"""
    return {
        "corner_radius": 8,
        "height": 35,
        "font": ("Segoe UI", 12)
    }

def get_entry_style():
    """Retorna estilo para campos de entrada"""
    return {
        "corner_radius": 8,
        "height": 35,
        "font": ("Segoe UI", 12)
    }

def get_frame_style():
    """Retorna estilo para frames"""
    return {
        "corner_radius": 10,
        "border_width": 0
    }
