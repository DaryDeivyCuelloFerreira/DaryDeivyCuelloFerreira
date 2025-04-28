import streamlit as st
import pandas as pd
import os
import socket
from datetime import datetime


# --- Diccionario de Carreras ---
carreras = {
    1: "Ciberseguridad",
    2: "Simulaciones Interactivas y Videojuegos",
    3: "Telecomunicaciones",
    4: "Inteligencia Artificial",
    5: "Informática Forense",
    6: "Energías Renovables",
    7: "Redes de Información",
    8: "Mecatrónica",
    9: "Manufactura Automatizada",
    10: "Manufactura Dispositivos Médicos",
    11: "Diseño Industrial",
    12: "Multimedia",
    13: "Sonido",
    14: "Desarrollo de Software",
    15: "Analítica y Ciencia de Datos",
    16: "Seguridad Informática"
}

# --- Profesores por materia ---
profesores_por_materia = {
    1: {  # Ciberseguridad
        "Procesos de Inf. Forense": ["David Santana Mejia", "Candido Noel Ramirez"],
        "Lab. Análisis Forense Digital II": ["Elkin Valenzuela Mateo"],
        "Lab. Análisis Forense Digital I": ["Elkin Valenzuela Mateo"],
        "Intro. a la Ciberseguridad": ["Carlos Edwin Rodriguez Cuevas", "Willy Alfredo Padua Ruiz", "Jose Manuel Doñe Mateo", "Jonathan Esteban Rondon Corniel", "Eric Combes", "Maria Antonia Pineda Pereyra", "Sucre Ramirez", "Gerald Williams Silvania Javiel", "Porfirio Marino Campaña Pérez"],
        "Análisis Forense Digital II": ["Elkin Valenzuela Mateo"],
        "Análisis Forense Digital I": ["Elkin Valenzuela Mateo"],
        "Análisis Forense de Malware": ["Elkin Valenzuela Mateo"],
        "Fundam. de Criptografía": ["Rafael Ovalle", "Manuel Guerrero", "Engel Antonio Rivas López", "Willy Alfredo Padua Ruiz", "Carlos Edwin Rodriguez Cuevas"],
        "Aspectos Legales de la Ciberseguridad": ["Maria Antonia Pineda Pereyra", "Joel Odalis Morrobel Ovalle", "Diogenes Jimenez"],
        "Seg. de Redes": ["Manuel Guerrero", "Jonathan Esteban Rondon Corniel", "Nelson Jose Mieses Hernandez"],
        "Seg. Avanzada en Redes": ["Manuel Guerrero"],
        "Seg. en Aplicaciones": ["Diogenes Jimenez", "Jorge Isaac Vanderhorst Ventura", "Adrian Alcantara", "Rafael Ovalle"],
        "Seg. de Sistemas Operativos": ["Engel Antonio Rivas López", "Carlos Edwin Rodriguez Cuevas", "Rafael Ovalle", "Juan Alexander Ramirez Perez"],
        "Intro. a la Ciencia Forense": ["Candido Noel Ramirez", "David Santana Mejia"],
        "Gestión de la Continuidad del Negocio": ["Arnaldo Andres Abreu Rosa", "Jorge Isaac Vanderhorst Ventura", "Rafael Ovalle"],
        "Auditoría de Seg. Informática": ["Jorge Isaac Vanderhorst Ventura", "Joel Andres Cuello Montero"],
        "Informática Forense": ["Jorge Isaac Vanderhorst Ventura", "David Santana Mejia"],
        "Desarrollo de Políticas y Proc. de Seg.": ["Willy Alfredo Padua Ruiz", "Joel Andres Cuello Montero", "Maria Antonia Pineda Pereyra", "Eric Combes"],
        "Gestión de Riesgos Tec. y Cibernéticos": ["Willy Alfredo Padua Ruiz", "Joel Andres Cuello Montero", "Carlos Edwin Rodriguez Cuevas"],
        "Hacker Ético II": ["Carlos Edwin Rodriguez Cuevas", "Diogenes Jimenez"],
        "Hacker Ético I": ["Nelson Jose Mieses Hernandez", "Diogenes Jimenez"],
        "Seguridad en la Nube": ["Raymund Johan Manuel Mejía Mercedes"],
        "Métodos y Herramientas Anti-Forense": ["David Santana Mejia"],
        "Forensia en Vivo": ["David Santana Mejia"],
        "Lab. Gestión de Evidencia Digital I": ["David Santana Mejia"],
        "Gestión de Evidencia Digital I": ["David Santana Mejia"],
        "Informe Técnico Pericial": ["Candido Noel Ramirez"],
        "Lab. Gestión de Evidencia Digital II": ["Candido Noel Ramirez"],
        "Gestión de Evidencia Digital II": ["Candido Noel Ramirez"],
        "Marco Legal y Normativa Forense": ["Candido Noel Ramirez"],
        "Proyecto Final TSI": ["Joel Andres Cuello Montero", "Nelson Jose Mieses Hernandez"],
        "Proyecto Final TIF": ["Elkin Valenzuela Mateo"],
        "Intro. a la seg. informática": ["Patricia Torres Diaz"]
    },
    2: {  # Simulaciones Interactivas y Videojuegos
        "Diseño de Niveles I - 3D": ["Milaysi De La Cruz Coronado", "Carlo Russo"],
        "Publicación en Plataformas Modernas": ["Frederick Ventura Lalondríz"],
        "Publicación en Plataformas Móviles": ["Frederick Ventura Lalondríz"],
        "Proyecto Final": ["Joel Valdez", "Alan Ricardo Franco Santana"],
        "Propiedad Intelectual y Derechos de Autor": ["Kelmer Emmanuel Messina Cruz"],
        "Pretotipo y Prototipo en Ideas": ["Virginia Peguero Tavarez"],
        "Segmentación de Usuarios": ["Virginia Peguero Tavarez"],
        "Intro. a la producción digital": ["Milaysi De La Cruz Coronado", "Carlo Russo"],
        "Diseño de Interfaz de Usuario": ["Milaysi De La Cruz Coronado"],
        "Presentación Creativa de Proyectos": ["Milaysi De La Cruz Coronado"],
        "Fundamentos de Música y Diseño de Sonido": ["Carlos José Mendoza"],
        "IA para Simulaciones": ["Alan Ricardo Franco Santana"],
        "Desarrollo de Simulaciones Interactivas": ["Alan Ricardo Franco Santana"],
        "Programación de Simulaciones": ["Alan Ricardo Franco Santana"],
        "Diseño de Niveles II - 2D": ["Alan Ricardo Franco Santana", "Lizandro Asahel Orozco Branagan"],
        "Estudio del Diseño de Videojuegos": ["Alan Ricardo Franco Santana"],
        "Programación de Videojuegos I - 3D": ["Lizandro Orozco"],
        "Programación de Videojuegos II - 2D": ["Lizandro Orozco"],
        "Diseño de Sprites y Gráficos 2D": ["Lizandro Orozco"]
    },
    4: {  # Inteligencia Artificial
    "Aprendizaje Profundo": [
        "Adan Javier Hernandez"
    ],
    "Lenguajes de Programación para IA": [
        "Adan Javier Hernandez", "Rina Maria Familia"
    ],
    "Planificación Inteligente": [
        "Jorge Luis Ledesma Urena"
    ],
    "Procesamiento del Lenguaje Natural": [
        "Rina Maria Familia", "Carlos Bienvenido Ogando Montas"
    ],
    "Álgebra Matricial": [
        "Ramon Emmanuel Alvarez Santana", "Risaldy Jose Rodriguez Jimenez"
    ],
    "Python": [
        "Bismark Montero", "Persio Martinez", "Hector Jeancarlos Santos Nuesi"
    ],
    "Bases de Datos: Diseño e Implementación": [
        "Persio Martinez", "Gregory Guillermo De La Rosa", "José Arcadio García García"
    ],
    "Matemáticas Discretas": [
        "Esloban Alberto Mora Vega", "Rina Maria Familia"
    ],
    "Estadística Avanzada": [
        "Esloban Alberto Mora Vega", "Nerbin Noel Jimenez German"
    ],
    "Modelado de Agentes Inteligentes": [
        "Adan Javier Hernandez", "Rina Maria Familia"
    ],
    "Lógica Matemática": [
        "Risaldy Jose Rodriguez Jimenez", "Ramon Emmanuel Alvarez Santana", "Carlos Bienvenido Ogando Montas"
    ],
    "Inteligencia Artificial": [
        "Risaldy Jose Rodriguez Jimenez", "Ever Miguel Curiel Morán", "Jean Charly Joseph Saint",
        "Marisol Alvarez Salcedo", "Luis Bessewell Feliz", "Carlos Bienvenido Ogando Montas",
        "Jorge Ramon Taveras González", "Rina Maria Familia"
    ],
    "IA e IoT": [
        "Luis Bessewell Feliz"
    ],
    "Seminario I": [
        "Luis Bessewell Feliz", "Rolando Oscar Garcia Guzman"
    ],
    "Introducción a la Inteligencia Artificial": [
        "Luis Bessewell Feliz", "Rina Maria Familia"
    ],
    "Juegos Inteligentes": [
        "Carlos Bienvenido Ogando Montas"
    ],
    "Inteligencia Artificial Distribuida": [
        "Carlos Bienvenido Ogando Montas"
    ],
    "Seminario II": [
        "Ramón Mena"
    ],
    "Proyecto Final TIA": [
        "Rina Maria Familia"
    ],
    "Robótica Inteligente": [
        "Rina Maria Familia"
    ],
    "Modelos de Representación del Conocimiento y el Razonamiento": [
        "Rina Maria Familia"
    ]
},


    7: {  # Redes de Información
    "Fundamentos de Redes": [
        "Lisbeth Jaquez", "Tomás Rodriguez", "Ruth Esther Santana Marte", "Samuel Ruíz De La Cruz", 
        "Bienvenida Consuegra Bidó", "Maria Antonia Pineda Pereyra", "Gerald Williams Silvania Javiel", 
        "Alejandro Andrés Garrido Aranda"
    ],
    "Fundamentos de Seguridad": [
        "Porfirio Marino Campaña Pérez", "Joel Odalis Morrobel Ovalle", "Willy Alfredo Padua Ruiz", 
        "Patricia Torres Diaz", "Ashley Stacy Mendez Martinez", "Adrian Alcantara", "Candido Noel Ramirez", 
        "Nicanor Peguero Garcia", "Saira Teresa Isaac Hernandez"
    ],
    "Fundamentos del Computador": [
        "Loida Eunice Charles Ramírez", "Juan Carlos Ramos Feliz", "Gleivis Francisco Ventura Cruz",
        "Mario De Jesus Guzman Cabral", "Kelvin Albuéz Blanco", "Richard Omar Jimenez Paredes",
        "Jean Luis Gonzalez Bautista", "Samuel Ignacio Sanchez Alvarez", "Bienvenida Consuegra Bidó",
        "Jesus Nicolas Mejia Ortiz", "Gabriel Antonio Perez De Los Santos", "Lionela Cabrera Santana",
        "Gerald Williams Silvania Javiel", "Porfirio Marino Campaña Pérez", "Jose Manuel Doñe Mateo"
    ],
    "Sistemas Operativos": [
        "Jean Luis Gonzalez Bautista", "Gleivis Francisco Ventura Cruz", "Mario De Jesus Guzman Cabral",
        "Samuel Ignacio Sanchez Alvarez", "Gerald Williams Silvania Javiel", "Porfirio Marino Campaña Pérez",
        "Jesus Nicolas Mejia Ortiz", "Onel Luis Pelegrino"
    ],
    "Instalación de Redes": [
        "Jose Manuel Doñe Mateo"
    ],
    "Introducción al Diseño de Redes": [
        "Manuel Guerrero"
    ],
    "Pasantía": [
        "Maria Antonia Pineda Pereyra"
    ],
    "Sistemas Operativos III": [
        "Tomás Rodriguez", "Onel Luis Pelegrino", "Samuel Ruíz De La Cruz", "Arnaldo Andres Abreu Rosa",
        "Adrian Alcantara", "Orlangel De La Rosa Modesto"
    ],
    "Introducción A Los Sistemas De Computación I": [
        "Gregory Guillermo De La Rosa"
    ],
    "Tecnologías WAN": [
        "Tomás Rodriguez"
    ],
    "Conmutación y Enrutamiento": [
        "Tomás Rodriguez", "Kelvin Albuéz Blanco", "Onel Luis Pelegrino", "Alejandro Andrés Garrido Aranda"
    ],
    "Laboratorio Conmutación y Enrutamiento": [
        "Cristian Cesarin Cornielle Ramirez", "Victor Manuel Mena Muñoz", "Alejandro Andrés Garrido Aranda",
        "Teofilo Antonio Díaz Pratt"
    ],
    "Laboratorio Fundamentos de Enrutamiento": [
        "Cristian Cesarin Cornielle Ramirez", "Victor Manuel Mena Muñoz", "Teofilo Antonio Díaz Pratt"
    ],
    "Fundamentos de Enrutamiento": [
        "Teofilo Antonio Díaz Pratt", "Onel Luis Pelegrino", "Samuel Ruíz De La Cruz",
        "Gamalier Sanchez Javier", "Maria Antonia Pineda Pereyra", "Alejandro Andrés Garrido Aranda"
    ],
    "Redacción Castellana": [
        "Maribel Jimenez Barrios"
    ],
    "Redes Inalámbricas": [
        "Orlangel De La Rosa Modesto"
    ],
    "Enrutamiento Avanzado": [
        "Orlangel De La Rosa Modesto"
    ],
    "Electiva I": [
        "Rafael Ovalle"
    ],
    "Electiva II": [
        "Rafael Ovalle"
    ],
    "Contabilidad Financiera": [
        "Aida Maria Vizcaino Rosario", "Abner Junior Villavicencio Frias",
        "Ricardo Moreno Diaz", "Lizmaida Alcala Calcaño"
    ],
    "Administración I": [
        "Ricardo Moreno Diaz"
    ],
    "Introducción a la Gerencia de Proyectos": [
        "Sucre Ramirez", "Virginia Mercedes Rymer Pérez", "Lizmaida Alcala Calcaño"
    ],
    "Gerencia de Proyectos de Tecnología de Información": [
        "Virginia Mercedes Rymer Pérez"
    ],
    "Proyecto Final TRI": [
        "Tomás Rodriguez"
    ]
},
15: {  # Analítica y Ciencia de Datos
    "Analítica Predictiva": [
        "Luis José Mota Nolasco", "Esloban Alberto Mora Vega"
    ],
    "Analítica Predictiva II": [
        "Luis José Mota Nolasco"
    ],
    "Base de Datos II": [
        "Héctor Jeancarlos Santos", "Persio Martinez"
    ],
    "Base de Datos I": [
        "José Arcadio García García", "Rolando Oscar Garcia Guzman",
        "José Manuel Aquino Cepeda"
    ],
    "Base de Datos III": [
        "José Manuel Aquino Cepeda", "Rolando Oscar Garcia Guzman"
    ],
    "Base de Datos Avanzada": [
        "Erick Leonardo Perez Veloz"
    ],
    "Introducción a la Analítica de Datos": [
        "Bismark Montero", "Ezequiel Díaz Montilla", 
        "Gregory Guillermo De La Rosa", "Ezequiel Díaz Montilla"
    ],
    "Introducción a la Base de Datos": [
        "Ezequiel Díaz Montilla", "Angel Ramón Batista",
        "Rolando Oscar Garcia Guzman"
    ],
    "Introducción a la Estadística": [
        "Esloban Alberto Mora Vega", "Ezequiel Díaz Montilla", 
        "Luis Bryan Mota Nolasco"
    ],
    "Analítica Descriptiva I": [
        "Esloban Alberto Mora Vega", "Nerbin Noel Jimenez German", 
        "Ezequiel Díaz Montilla", "Luis José Mota Nolasco"
    ],
    "Analítica Descriptiva II": [
        "Maria Tatiana Burgos Castillo", "Kelyn Tejada Belliard"
    ],
    "Analítica Descriptiva III": [
        "Esloban Alberto Mora Vega", "José Arcadio García García"
    ],
    "Analítica Prescriptiva I": [
        "Esloban Alberto Mora Vega"
    ],
    "Analítica de Datos para Finanzas (Optativa II)": [
        "Gregory Guillermo De La Rosa", "Luis José Mota Nolasco"
    ],
    "Análisis de Datos con Excel": [
        "Gregory Guillermo De La Rosa", "Angel Ramón Batista"
    ],
    "Procesadores de Textos y Técnicas de Informes": [
        "Kelyn Tejada Belliard", "José Arcadio García García", 
        "Luis José Mota Nolasco"
    ],
    "Introducción a los Sistemas de Computación I": [
        "José Manuel Aquino Cepeda", "Rolando Oscar Garcia Guzman",
        "Gregory Guillermo De La Rosa"
    ],
    "Introducción a los Sistemas de Computación II": [
        "Jean Charly Joseph Saint", "Adan Javier Hernandez"
    ],
    "Introducción a los Sistemas de Representación": [
        "Jorge Ramon Taveras González", "Gregory Guillermo De La Rosa",
        "Rolando Oscar Garcia Guzman"
    ],
    "Programación I": [
        "José Arcadio García García", "Jean Charly Joseph Saint"
    ],
    "Programación II": [
        "Jean Charly Joseph Saint", "Adan Javier Hernandez"
    ],
    "Programación III": [
        "José Manuel Aquino Cepeda"
    ],
    "Programación IV": [
        "Jean Charly Joseph Saint", "José Arcadio García García"
    ],
    "Proyecto Final TCD": [
        "José Manuel Aquino Cepeda"
    ],
    "Introducción a las Ciencias de los Datos": [
        "José Manuel Aquino Cepeda", "Ramón Mena"
    ]
},
12: {  # Multimedia
    "Introducción al DAW": [
        "Alberto Moreta Martinez", "Bryan Ramon Paniagua Martinez"
    ],
    "Laboratorio Introducción al DAW": [
        "Alberto Moreta Martinez", "Bryan Ramon Paniagua Martinez"
    ],
    "Estadística Básica": [
        "Maria Tatiana Burgos Castillo", "Santo Figueroa", "Nerbin Noel Jimenez German"
    ],
    "Sonido para Audiovisuales": [
        "Alfio Lora", "Alberto Moreta Martinez"
    ],
    "Sonido para Cine": [
        "Susan Romero"
    ],
    "Mesa de Mezcla I": [
        "Moises Gonzalez Salazar", "Alberto Moreta Martinez"
    ],
    "Mesa de Mezcla II": [
        "Moises Gonzalez Salazar"
    ],
    "Psicoacústica": [
        "Moises Gonzalez Salazar"
    ],
    "DAW Avanzado": [
        "Moises Gonzalez Salazar"
    ],
    "MIDI": [
        "Moises Gonzalez Salazar"
    ],
    "Comunicación Visual Avanzada": [
        "Yasmery Gomez", "Daigoro Ricardo Sanchez Valoy"
    ],
    "Introducción Comunicación Visual": [
        "Nestor Gautreaux", "Yasmery Gomez"
    ],
    "Gráficos de Mapa de Bits": [
        "Yasmery Gomez", "Francisco Alberto Caamaño Tawil", "Daigoro Ricardo Sanchez Valoy",
        "Francisco Alberto Garcia De Leon", "Nestor Gautreaux", "Jonathan Albuez", 
        "Werner Froilan Olmos Tavàrez", "Teovianny Emil Rodríguez Sarita"
    ],
    "Fotografía": [
        "Nestor Gautreaux", "Driade Judith Pared Diaz"
    ],
    "Animación 2D": [
        "Walky Antonio Abreu Lara", "Brayan Alberto Acosta Pool"
    ],
    "Laboratorio de Animación 2D": [
        "Walky Antonio Abreu Lara"
    ],
    "Audio Digital": [
        "Carlos José Mendoza", "Starlin Franco Basilis", "Susan Romero"
    ],
    "Audio Digital Avanzado": [
        "Starlin Franco Basilis", "Carlos José Mendoza", "Bryan Ramon Paniagua Martinez"
    ],
    "Programación Web": [
        "Jeremy Guzman Mendoza", "Rolando Oscar Garcia Guzman", "Valentin Sanchez Estevez"
    ],
    "HTML y Creación de Web Sites": [
        "Jeremy Guzman Mendoza", "Rolando Oscar Garcia Guzman"
    ],
    "Dibujo Técnico": [
        "Johanna Dovil Calix De Báez", "Francisco Ramirez Velasquez"
    ],
    "Marketing": [
        "Carlos Manuel Vargas Toledo", "Vladimir Columna Pimentel"
    ],
    "Gestion Empresarial Publicitaria": [
        "Carlos Manuel Vargas Toledo", "Vladimir Columna Pimentel"
    ],
    "Publicidad": [
        "Mario Disla", "Ramón Alfonso Matos Galán"
    ],
    "Plan de Negocios": [
        "Sandra María González Martínez", "Aurora Aquino", "Lizmaida Alcala Calcaño"
    ],
    "Interactividad": [
        "Denisse Peralta Encarnación", "Jeremy Guzman Mendoza"
    ],
    "Ilustración Digital": [
        "Robin Elias Salas García", "Werner Froilan Olmos Tavàrez"
    ],
    "Dibujo e Ilustración": [
        "Carmen Luisa Valerio Díaz", "Virginia Peguero Tavarez", "Nestor Gautreaux"
    ],
    "Electiva 1": [
        "Robin Elias Salas García", "Tony Bacigaluppe Perez", "Susan Romero"
    ],
    "Electiva 2": [
        "Walky Antonio Abreu Lara", "Bianna Peña Rubio", "Tony Bacigaluppe Pérez"
    ],
    "Producción musical": [
        "Alfio Lora"
    ],
    "Locución comercial": [
        "Vladimir Columna Pimentel"
    ],
    "Acústica arquitectónica": [
        "Alfio Lora"
    ],
    "Audio Digital Avanzado (Virtual)": [
        "Carlos José Mendoza"
    ],
    "Introducción a Multimedia": [
        "Brayan Alberto Acosta Pool", "Leandro Marte Geraldino", 
        "Franklin Ulises Cedeno Villavicencio", "Miguel Aquiles Nina Javier", 
        "Jonathan Albuez"
    ],
    "Diseño y Maquetación de Interfaz": [
        "Francisco Alberto Garcia De Leon"
    ],
    "Diseño de Empaque": [
        "Adrian Joseph Medrano Marquez"
    ],
    "Producción Audio Visual": [
        "Tony Bacigaluppe Perez", "Luisa Gerardina Suzaña Perez"
    ],
    "Motion Graphics y Efectos Visuales": [
        "Brayan Alberto Acosta Pool"
    ],
    "Edición y post- Producción de Vídeo": [
        "Tony Bacigaluppe Perez", "Brayan Alberto Acosta Pool"
    ],
    "Industria de la Música": [
        "Francisco Alberto Caamaño Tawil"
    ],
    "Electrónica del Audio": [
        "Tiziano Fajardo"
    ],
    "Razonamiento Crítico": [
        "Juan De Jesus Rodriguez Ortiz", "Jose Ernesto Flete Morillo"
    ],
    "Sonido en Vivo": [
        "Alberto Moreta Martinez"
    ],
    "Síntesis de Sonido": [
        "Alberto Moreta Martinez"
    ],
    "Entrenamiento auditivo musical": [
        "Bryan Ramon Paniagua Martinez"
    ],
    "Teoría Musical": [
        "Bryan Ramon Paniagua Martinez"
    ],
    "Teoría Musical II": [
        "Bryan Ramon Paniagua Martinez"
    ],
    "Introducción al Piano": [
        "Bryan Ramon Paniagua Martinez"
    ],
    "Introducción a la Música": [
        "Bryan Ramon Paniagua Martinez"
    ],
    "3D Modelado y Renderizado": [
        "Gabriel Ortiz Magarin", "Carlo Russo"
    ],
    "3D Luces y Texturas": [
        "Gabriel Ortiz Magarin"
    ],
    "3D Creación de Personaje y Animación": [
        "Antonio Bonilla"
    ],
    "Laboratorio de 3D luces y Textura": [
        "Gabriel Ortiz Magarin", "Antonio Bonilla"
    ],
    "Laboratorio de 3D Creación de Personaje y Animación": [
        "Antonio Bonilla"
    ],
    "Desktop Publishing Avanzado": [
        "Mario Disla", "Teovianny Emil Rodríguez Sarita"
    ],
    "Introducción a Desktop Publishing": [
        "Franklin Ulises Cedeno Villavicencio", "Teovianny Emil Rodríguez Sarita"
    ]
},
14: {  # Software y Bases de Datos
    "Minería de Datos e Inteligencia de Negocios": [
        "Juan Restituyo", "Leandro Fondeur Gil", "Eduandy Isabel Cruz Abreu", "Jorge Ramon Taveras González"
    ],
    "Introducción a las bases de Datos": [
        "José Luis Encarnación Ravelo", "Carlos Manuel Caraballo", "Francisco Genao",
        "Angel Ramón Batista", "Gilberto Elias Vittini", "Lucy Mendez", "Mauren Llunirsa Orozco Hurtado",
        "Geraldo Peralta Bidó", "Freidy Nunez Perez", "Aneury Fortunato", "Ezequiel Díaz Montilla"
    ],
    "Introducción a la elaboración de Algoritmos": [
        "Juan Restituyo", "Freidy Nunez Perez", "Francisco Genao", "Ever Miguel Curiel Morán",
        "José Luis Encarnación Ravelo", "Mauren Llunirsa Orozco Hurtado", "Gilberto Elias Vittini",
        "Aneury Fortunato", "Carlos Daniel Fernandez Rodriguez", "Marisol Alvarez Salcedo",
        "Orison Soto", "Jean Charly Joseph Saint", "Lucy Mendez", "Cibeles Tavarez",
        "Jose Antonio De Jesus Alcantara", "Wilmer Jose Fariña Piñero", "Yovanny Yudelis Castillo Cuello"
    ],
    "Diseño Centrado en el Usuario": [
        "Jorge Ramon Taveraz Gonzalez", "Juan Martínez López", "Ricardo Acosta", "Juan Restituyo"
    ],
    "Administración de Proyectos de Software": [
        "Jesus Maria Quezada", "Willis Ezequiel Polanco Caraballo", "Francisco Genao",
        "Silvano Saul Estévez Gómez", "Orison Soto"
    ],
    "Programación II": [
        "Bismark Montero", "Adan Javier Hernandez", "Juan Enmanuel Rosario Rodriguez",
        "Eduandy Isabel Cruz Abreu", "Jose Antonio De Jesus Alcantara", "Francis Ramirez",
        "Michael Grullon", "Luis Soto Mirambeaux"
    ],
    "Introducción a la Ingeniería de Software": [
        "Evanyeline Brito Rojas", "Ever Miguel Curiel Morán", "Eduandy Isabel Cruz Abreu",
        "Valentin Sanchez Estevez"
    ],
    "Base de Datos Avanzada": [
        "Evanyeline Brito Rojas", "Leandro Fondeur Gil", "Carlos Manuel Caraballo", "Geraldo Peralta Bidó"
    ],
    "Programación III": [
        "Kelyn Tejada Belliard", "Eduandy Isabel Cruz Abreu", "Leonardo Enrique Tavarez Betances",
        "Ricardo Acosta"
    ],
    "Programación I": [
        "Kelyn Tejada Belliard", "Ricardo Acosta", "Jean Charly Joseph Saint", "Luis Soto Mirambeaux",
        "Freidy Nunez Perez"
    ],
    "Fundamentos de Programación": [
        "Persio Martinez", "Juan Enmanuel Rosario Rodriguez", "Aneury Fortunato", 
        "Jose Abreu Sanchez", "Orison Soto", "Wilmer Jose Fariña Piñero"
    ],
    "Programación Paralela": [
        "Erick Leonardo Perez Veloz", "Mauren Llunirsa Orozco Hurtado", "Wilmer Jose Fariña Piñero"
    ],
    "Introducción al Desarrollo de Aplicaciones Móviles": [
        "Amadis Suarez Genao", "Freidy Nunez Perez", "Michael Grullon"
    ],
    "Análisis y Diseño de Sistemas": [
        "Simeon Clase Ulloa", "Mauren Llunirsa Orozco Hurtado", "Daniel Parra", "Cibeles Tavarez",
        "Lucy Mendez"
    ],
    "Programación Web": [
        "Luis Soto Mirambeaux", "Daniel Parra", "Raydelto Hernández Perera", "Amadis Suarez Genao"
    ],
    "Estructura de Datos": [
        "Raydelto Hernández Perera", "Eduandy Isabel Cruz Abreu", "Michael Grullon"
    ],
    "Electiva 1": [
        "Elvys Cruz", "Francis Ramirez", "Michael Grullon"
    ],
    "Electiva 2": [
        "Elvys Cruz", "Francis Ramirez"
    ],
    "Auditoría Informática": [
        "Jesus Maria Quezada", "Cibeles Tavarez", "Carlos Daniel Fernandez Rodriguez"
    ],
    "Proyecto Final TDS": [
        "Willis Ezequiel Polanco Caraballo", "Huascar Frias Vilorio"
    ]
}


}


# --- Crear df_tecnicos basado en profesores_por_materia ---
datos_tecnicos = {
    "Carrera": [],
    "Asignatura": [],
    "Nombre": []
}

for id_carrera, materias in profesores_por_materia.items():
    nombre_carrera = carreras.get(id_carrera, "Desconocido")
    for materia, profesores in materias.items():
        for profesor in profesores:
            datos_tecnicos["Carrera"].append(nombre_carrera)
            datos_tecnicos["Asignatura"].append(materia)
            datos_tecnicos["Nombre"].append(profesor)

df_tecnicos = pd.DataFrame(datos_tecnicos)

# --- Inicializar usuario ---
if 'usuario' not in st.session_state:
    st.session_state['usuario'] = None

# --- Archivos ---
archivo_calif = 'calificaciones.csv'
archivo_usuarios = 'usuarios.csv'

user_ip = socket.gethostname()

# --- Cargar archivos ---
if os.path.exists(archivo_calif):
    df_calificaciones = pd.read_csv(archivo_calif)
else:
    df_calificaciones = pd.DataFrame(columns=['Carrera', 'Asignatura', 'Nombre', 'Ranking'])

if os.path.exists(archivo_usuarios):
    df_usuarios = pd.read_csv(archivo_usuarios)
else:
    df_usuarios = pd.DataFrame(columns=['nombre_usuario', 'email', 'password', 'votos', 'ip', 'carrera', 'votados'])


# --- Funciones auxiliares ---
def preparar_tabla(df):
    df = df.dropna(subset=['Ranking'])
    df['Ranking'] = pd.to_numeric(df['Ranking'], errors='coerce')
    df_ordenado = df.sort_values(by='Ranking', ascending=False).reset_index(drop=True)
    df_ordenado['Ranking'] = df_ordenado['Ranking'].round(1)
    medallas = []
    for ranking in df_ordenado['Ranking']:
        if ranking >= 4.5:
            medallas.append('🥇 Oro')
        elif 4.1 <= ranking < 4.5:
            medallas.append('🥈 Plata')
        elif 3.8 <= ranking < 4.1:
            medallas.append('🥉 Bronce')
        else:
            medallas.append('-')
    df_ordenado['Medalla'] = medallas
    return df_ordenado[['Carrera', 'Nombre', 'Asignatura', 'Ranking', 'Medalla']]

def aplicar_estilos(df):
    def estilo(val):
        if val == '🥇 Oro':
            return 'background-color: gold; color: black; font-weight: bold'
        if val == '🥈 Plata':
            return 'background-color: silver; color: black; font-weight: bold'
        if val == '🥉 Bronce':
            return 'background-color: #cd7f32; color: white; font-weight: bold'
        return ''
    return df.style.applymap(estilo, subset=['Medalla'])

def iniciar_sesion(usuario):
    st.session_state['usuario'] = usuario

def cerrar_sesion():
    st.session_state['usuario'] = None


# --- INTERFAZ ---
st.title('🏅 Ranking de Rendimiento Docente')

if st.session_state.usuario:
    st.sidebar.markdown(f"👤 {st.session_state.usuario}")

st.sidebar.header("Navegación")
seccion = st.sidebar.radio('Seleccione:', ['Seleccione una opción', 'Técnicos', 'Registrar Cuenta', 'Login', 'Calificar'])

carreras_con_profes = sorted(df_tecnicos['Carrera'].unique())

if seccion == 'Técnicos':
    carrera = st.sidebar.selectbox('Seleccione Técnico:', carreras_con_profes)
    if carrera:
        df_filtrado = df_tecnicos[df_tecnicos['Carrera'] == carrera]
        df_filtrado = pd.merge(df_filtrado, df_calificaciones, on=['Carrera', 'Asignatura', 'Nombre'], how='left')

        asignaturas = sorted(df_filtrado['Asignatura'].unique())
        asignatura = st.sidebar.selectbox('Seleccione Asignatura:', ['Todas'] + asignaturas)

        if asignatura != 'Todas':
            df_filtrado = df_filtrado[df_filtrado['Asignatura'] == asignatura]

        buscar = st.sidebar.text_input('Buscar profesor')
        if buscar:
            df_filtrado = df_filtrado[df_filtrado['Nombre'].str.contains(buscar, case=False)]

        if not df_filtrado.empty:
            st.dataframe(aplicar_estilos(preparar_tabla(df_filtrado)).format({'Ranking': '{:.1f}'}))
        else:
            st.info('No hay resultados.')

elif seccion == 'Registrar Cuenta':
    st.subheader("Crear cuenta nueva")
    nombre_usuario = st.text_input("Usuario")
    email = st.text_input("Correo")
    password = st.text_input("Contraseña", type="password")
    carrera = st.selectbox('Seleccione su Técnico:', carreras_con_profes)

    if st.button("Registrar"):
        if nombre_usuario and email and password and carrera:
            if user_ip in df_usuarios['ip'].dropna().values:
                st.error("Este dispositivo ya está registrado.")
            elif email.strip() in df_usuarios['email'].astype(str).str.strip().values:
                st.error("Correo ya registrado.")
            else:
                nuevo = pd.DataFrame({
                    'nombre_usuario': [nombre_usuario.strip()],
                    'email': [email.strip()],
                    'password': [password.strip()],
                    'votos': [5],
                    'ip': [user_ip],
                    'carrera': [carrera],
                    'votados': [None]
                })
                df_usuarios = pd.concat([df_usuarios, nuevo], ignore_index=True)
                df_usuarios.to_csv(archivo_usuarios, index=False)
                st.success("¡Registrado exitosamente!")
        else:
            st.warning("Completa todo por favor.")

elif seccion == 'Login':
    st.subheader("Iniciar sesión")
    email = st.text_input("Correo", key="email_login")
    password = st.text_input("Contraseña", type="password", key="pass_login")

    if st.button("Login"):
        user = df_usuarios[(df_usuarios['email'].astype(str).str.strip() == email.strip()) &
                           (df_usuarios['password'].astype(str).str.strip() == password.strip())]
        if not user.empty:
            iniciar_sesion(user.iloc[0]['nombre_usuario'])
            st.success(f"Bienvenido {user.iloc[0]['nombre_usuario']}")
        else:
            st.error("Correo o contraseña incorrectos.")

elif seccion == 'Calificar':
    if not st.session_state.usuario:
        st.warning("Debes iniciar sesión para calificar.")
    else:
        df_usuarios = pd.read_csv(archivo_usuarios)
        user_row = df_usuarios[df_usuarios['nombre_usuario'] == st.session_state.usuario].iloc[0]
        votos = user_row['votos']
        carrera_usuario = user_row['carrera']

        st.subheader(f"🎓 Carrera: {carrera_usuario}")
        votados = [] if pd.isna(user_row['votados']) else user_row['votados'].split(';')

        st.info(f"🔵 Te quedan {votos} votos disponibles.")

        if votos <= 0:
            st.error("No tienes votos disponibles.")
        else:
            carrera_sel = carrera_usuario
            df_carrera = df_tecnicos[df_tecnicos['Carrera'] == carrera_sel]

            if df_carrera.empty:
                st.info('Esta carrera aún no tiene profesores para calificar.')
            else:
                asignaturas = sorted(df_carrera['Asignatura'].unique())
                asignatura_sel = st.selectbox('Materia:', asignaturas)
                profesores = sorted(df_carrera[df_carrera['Asignatura'] == asignatura_sel]['Nombre'].unique())
                profesor_sel = st.selectbox('Profesor:', profesores)

                identificador = f"{profesor_sel}-{asignatura_sel}"
                if identificador in votados:
                    st.warning("Ya calificaste a este profesor en esta materia.")
                else:
                    preguntas = [
                        "Claridad al explicar",
                        "Dominio del contenido",
                        "Estructura de clases",
                        "Participación estudiantil",
                        "Resolución de dudas",
                        "Puntualidad",
                        "Interés en el aprendizaje",
                        "Uso de recursos",
                        "Respeto en aula",
                        "¿Lo recomendarías?"
                    ]
                    respuestas = [st.slider(p, 1, 5, 3) for p in preguntas]
                    if st.button("Enviar Calificación"):
                        promedio = sum(respuestas) / len(respuestas)
                        nueva = {'Carrera': carrera_sel, 'Asignatura': asignatura_sel, 'Nombre': profesor_sel, 'Ranking': promedio}

                        mask = (
                            (df_calificaciones['Carrera'] == carrera_sel) &
                            (df_calificaciones['Asignatura'] == asignatura_sel) &
                            (df_calificaciones['Nombre'] == profesor_sel)
                        )

                        if mask.any():
                            existente = df_calificaciones.loc[mask, 'Ranking'].values[0]
                            nuevo = (existente + promedio) / 2
                            df_calificaciones.loc[mask, 'Ranking'] = nuevo
                        else:
                            df_calificaciones = pd.concat([df_calificaciones, pd.DataFrame([nueva])], ignore_index=True)

                        df_calificaciones.to_csv(archivo_calif, index=False)
                        df_usuarios.loc[df_usuarios['nombre_usuario'] == st.session_state.usuario, 'votos'] -= 1
                        nuevos_votados = ';'.join(votados + [identificador])
                        df_usuarios.loc[df_usuarios['nombre_usuario'] == st.session_state.usuario, 'votados'] = nuevos_votados
                        df_usuarios.to_csv(archivo_usuarios, index=False)
                        st.success("✅ Calificación enviada. ¡Gracias!")