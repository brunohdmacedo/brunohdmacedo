from tqdm import tqdm
import time

# Simula as etapas de cálculo de métricas
total_steps = 50  # Número de etapas da cobrinha
for i in tqdm(range(total_steps), desc="Cobrinha", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
    time.sleep(0.1)  # Simula um cálculo pesado, ajustando conforme necessário
