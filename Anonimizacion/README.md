# 🔒 Anonimización de Datos - Protección de Información Sensible

## 🎯 Objetivo

Aplicar técnicas de anonimización a una base de datos para proteger la identidad de los pacientes/usuarios, cumpliendo con principios de protección de datos personales.

## 🛠️ Técnicas aplicadas

| Técnica | Descripción | Aplicación en el código |
|---------|-------------|--------------------------|
| **Supresión** | Eliminar datos directamente identificables | Se eliminaron columnas: `Nombre completo`, `Teléfono` |
| **Generalización** | Reducir precisión de los datos | `Edad` → rangos (0-18, 19-30, 31-50, 51+)<br>`Código postal` → primeros 3 dígitos + "XX" |
| **Codificación** | Reemplazar texto por números | `Género`: Masculino→1, Femenino→2 |
| **Clasificación** | Agrupar categorías específicas en categorías generales | `Diagnóstico` → `Enfermedad metabólica`, `oncológica`, `respiratoria`, etc. |
| **Perturbación** | Agregar ruido aleatorio | `Ingresos anuales` + ruido normal (media 0, desviación 5) |
| **Seudonimización** | Reemplazar identificador directo por hash | `ID` = hash SHA256 del índice de fila |

## 📊 Flujo del proceso

1. Cargar base desde Excel (`Base de Datos.xlsx`)
2. Aplicar técnicas en orden lógico
3. Guardar nueva base anonimizada (`Base_Anonimizada.xlsx`)

## ▶️ Cómo ejecutar

```bash
python anonimizacion.py
