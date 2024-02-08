import tkinter as tk
import psutil

def atualizar_estatisticas(frame):
    # Limpar frame antes de atualizar
    for widget in frame.winfo_children():
        widget.destroy()

    # Exibir estatísticas da CPU
    cpu_label = tk.Label(frame, text="== Informações da CPU ==")
    cpu_label.pack(anchor="w")
    freq_label = tk.Label(frame, text=f"Frequência atual: {psutil.cpu_freq().current} MHz")
    freq_label.pack(anchor="w")
    uso_label = tk.Label(frame, text=f"Uso da CPU (%): {psutil.cpu_percent(interval=1)}")
    uso_label.pack(anchor="w")
    tempos_label = tk.Label(frame, text=f"Tempos da CPU: {psutil.cpu_times()}")
    tempos_label.pack(anchor="w")

    # Exibir estatísticas da Memória
    mem_label = tk.Label(frame, text="== Informações da Memória ==")
    mem_label.pack(anchor="w")
    mem_total_label = tk.Label(frame, text=f"Total: {psutil.virtual_memory().total} bytes")
    mem_total_label.pack(anchor="w")
    mem_disp_label = tk.Label(frame, text=f"Disponível: {psutil.virtual_memory().available} bytes")
    mem_disp_label.pack(anchor="w")
    mem_perc_label = tk.Label(frame, text=f"Percentual de uso: {psutil.virtual_memory().percent} %")
    mem_perc_label.pack(anchor="w")

    # Exibir estatísticas dos Discos
    disk_label = tk.Label(frame, text="== Informações dos Discos ==")
    disk_label.pack(anchor="w")
    disks = psutil.disk_partitions()
    for disk in disks:
        disk_info_label = tk.Label(frame, text=f"Dispositivo: {disk.device}, Montagem: {disk.mountpoint}, Tipo: {disk.fstype}")
        disk_info_label.pack(anchor="w")
        disk_usage_label = tk.Label(frame, text=f"Uso: {psutil.disk_usage(disk.mountpoint)}")
        disk_usage_label.pack(anchor="w")

    # Exibir estatísticas da Rede
    net_label = tk.Label(frame, text="== Informações da Rede ==")
    net_label.pack(anchor="w")
    net_stats_label = tk.Label(frame, text=f"Estatísticas de Rede: {psutil.net_io_counters()}")
    net_stats_label.pack(anchor="w")
    net_stats_per_label = tk.Label(frame, text="Estatísticas de Rede por Interface:")
    net_stats_per_label.pack(anchor="w")
    for interface, stats in psutil.net_io_counters(pernic=True).items():
        interface_label = tk.Label(frame, text=f"Interface: {interface}, Enviados: {stats.bytes_sent}, Recebidos: {stats.bytes_recv}")
        interface_label.pack(anchor="w")

def exibir_estatisticas():
    # Criar janela
    janela = tk.Tk()
    janela.title("Estatísticas do Sistema")

    # Frame para as estatísticas
    frame = tk.Frame(janela)
    frame.pack(padx=10, pady=10)

    # Atualizar estatísticas ao iniciar
    atualizar_estatisticas(frame)

    # Botão de atualização
    atualizar_btn = tk.Button(janela, text="Atualizar", command=lambda: atualizar_estatisticas(frame))
    atualizar_btn.pack(pady=10)

    # Iniciar loop da janela
    janela.mainloop()

if __name__ == "__main__":
    exibir_estatisticas()
