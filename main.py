import tkinter as tk
from tkinter import ttk

class Estacion:
    def __init__(self, nombre, componentes, estado):
        self.nombre = nombre
        self.componentes = componentes
        self.estado = tk.StringVar( value=estado)        

class InterfazMonitor:
    def __init__(self, master, estaciones):
        self.master = master
        self.master.title("Monitor de Verificación")
        #self.estaciones = [Estacion(**estacion) for estacion in estaciones]
    
        self.estaciones = [
            Estacion("Estación 1", [{"name": "Componente 1", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    {"name": "Componente 2", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    {"name": "Componente 3", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                     ], "Verificado"
                ),
            Estacion("Estación 2", [{"name": "Componente 4", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    {"name": "Componente 5", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    {"name": "Componente 6", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    {"name": "Componente 7", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    ], "Verificado"
                ),
            Estacion("Estación 3", [{"name": "Componente 8", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Pass"},
                                    {"name": "Componente 9", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"Missing"},
                                    ], "Missing component"
                ),
            Estacion("Estación 4", [{"name": "Componente 9", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"No yet"},
                                    {"name": "Componente 10", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"No yet"},
                                    ], "Proceso"
                ),
            Estacion("Estación 5", [{"name": "Componente 10", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"No yet"}], "Proceso"
                ),
            Estacion("Estación 6", [{"name": "Componente 11", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"No yet"}], "Proceso"
                ),
            Estacion("Estación 7", [{"name": "Componente 12", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"No yet"}], "Proceso"
                ),
            Estacion("Estación 8", [{"name": "Componente 13", "image_url": "https://i.imgur.com/4LQbQ8S.png","checkpoint":"No yet"}], "Proceso"
                ),
        ]

        self.crear_interfaz()

    def crear_interfaz(self):
        # Obtén la mitad de la cantidad de estaciones
        mitad = len(self.estaciones) // 2

        # Obtén el ancho y la altura de la pantalla
        ancho_pantalla = self.master.winfo_screenwidth()
        altura_pantalla = self.master.winfo_screenheight()

        for i, estacion in enumerate(self.estaciones):
            # Verificar el estado y definir el color del fondo del título
            color_fondo = ""
            if estacion.estado.get() == "Verificado":
                color_fondo = "green"
            elif estacion.estado.get() == "Proceso":
                color_fondo = "yellow"
            else:
                color_fondo = "red"
            frame_estacion = tk.Frame(self.master,  bg=color_fondo, bd=10, relief="groove", highlightbackground="black", highlightthickness=.5)

            # Ubicar el frame en la pantalla
            fila = i // mitad
            columna = i % mitad

            # Configura la fila y la columna para que se expandan y llenen el espacio disponible
            self.master.grid_rowconfigure(fila, weight=1)
            self.master.grid_columnconfigure(columna, weight=1)

            # Cambiar el tamaño de frame_estacion
            frame_estacion.grid(row=fila, column=columna, sticky="nsew")
            
            # Mostrar el estado de la estación
            tk.Label(frame_estacion, text="Estado:", bg= color_fondo).grid(row=1, column=0, sticky="w")         
            tk.Label(frame_estacion, textvariable=estacion.estado, bg= color_fondo).grid(row=1, column=1, sticky="w", padx=10, pady=10)
            # Mostrar el nombre de la estación
            label_frame = tk.Frame(frame_estacion, borderwidth=2, relief='raised', bg= 'white', highlightbackground="blue", highlightthickness=2)
            label_frame.grid(sticky="w", row=2, column=0, columnspan=3)
            label = tk.Label(label_frame, text=estacion.nombre, font=("Helvetica", 12, "bold"), bg= '#bcbfd0', foreground='blue', anchor="center")
            label.grid(sticky='e', row=2, column=0, padx=.5, pady=.5, columnspan=2)
            # Insertar una tabla con los componentes
            tabla_componentes = ttk.Treeview(frame_estacion, columns=("name", "checkpoint"), show="headings", selectmode="none")
            tabla_componentes.grid(row=5, column=0, sticky="nsew", columnspan=2)
            tabla_componentes.grid_columnconfigure(0, weight=5)
            tabla_componentes.grid_columnconfigure(1, weight=1)
            tabla_componentes.grid_rowconfigure(0, weight=1)
            tabla_componentes.grid_rowconfigure(1, weight=1)
            
            tabla_componentes.tag_configure("oddrow", background="white")
            tabla_componentes.tag_configure("evenrow", background="#bcbfd0")
            tabla_componentes.tag_configure('verificado', foreground='green')
            tabla_componentes.tag_configure('proceso', foreground="blue")
            tabla_componentes.tag_configure('fallo', foreground="red")
            tabla_componentes.heading("name", text="Componente", anchor="w", )
            tabla_componentes.heading("checkpoint", text="Checkpoint")
            for i, componente in enumerate(estacion.componentes):
                if i % 2 == 0:
                    if componente['checkpoint'] == "Pass":
                        tabla_componentes.insert("", tk.END, values=(componente["name"], componente["checkpoint"]), tags=('verificado','oddrow'))
                    elif componente['checkpoint'] == "No yet":
                        tabla_componentes.insert("", tk.END, values=(componente["name"], componente["checkpoint"]), tags=('proceso','oddrow'))
                    else:
                        tabla_componentes.insert("", tk.END, values=(componente["name"], componente["checkpoint"]), tags=('fallo','oddrow'))
                else:
                    if componente['checkpoint'] == "Pass":
                        tabla_componentes.insert("", tk.END, values=(componente["name"], componente["checkpoint"]), tags=('verificado','evenrow'))
                    elif componente['checkpoint'] == "No yet":
                        tabla_componentes.insert("", tk.END, values=(componente["name"], componente["checkpoint"]), tags=('proceso','evenrow'))
                    else:
                        tabla_componentes.insert("", tk.END, values=(componente["name"], componente["checkpoint"]), tags=('fallo','evenrow'))                    

if __name__ == "__main__":
    root = tk.Tk()
    estaciones = []
    app = InterfazMonitor(root, estaciones)
    
    style = ttk.Style()
    style.theme_use('clam') # ('clam', 'alt', 'default', 'classic')
    style.configure('TLabel', font=('Helvetica', 12, 'bold'), background="white", foreground="blue", color="blue", highlightthickness=5, relief="flat", selectbackground="blue", selectforeground="white", selectcolor="blue", bordercolor="blue", highlightcolor="blue", highlightbackground="blue", spacing1=0, spacing2=0, spacing3=0, padx=0, pady=0, indicatoron=0, selectmode="none", anchor="w", state="disabled", wrap="none",)
    style.configure('Treeview', font=('Helvetica', 10, 'bold',), rowheight=25, fieldbackground="#bcbfd0", background="#bcbfd0", foreground="blue", color="blue", highlightthickness=1, relief='solid', selectbackground="blue", selectforeground="#b3cce6", selectcolor="blue", bordercolor="blue", highlightcolor="blue", highlightbackground="blue", spacing1=0, spacing2=0, spacing3=0, padx=0, pady=0, indicatoron=0, selectmode="none", anchor="w", state="disabled", wrap="none",)
    


    # Pantalla completa
    root.attributes('-fullscreen', True)
    # Centrar la ventana
    ancho_pantalla = root.winfo_screenwidth()
    altura_pantalla = root.winfo_screenheight()
    root.geometry(f"{ancho_pantalla}x{altura_pantalla}+0+0")


    root.mainloop()
