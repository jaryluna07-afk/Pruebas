--
-- PostgreSQL database dump
--

\restrict 3PlRHzZCZ2ckZZr6nVvlGrfdKAwfSD0b3mK12BO1mhOQT2luKkEQpKpAC8499XD

-- Dumped from database version 18.3
-- Dumped by pg_dump version 18.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: core_rol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_rol (id, nombre_rol) FROM stdin;
1	Administrador
2	Usuario
\.


--
-- Data for Name: core_tipocontacto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_tipocontacto (id, nombre_tipo) FROM stdin;
1	Persona Natural
2	Persona Jurídica
\.


--
-- Data for Name: core_tipoidentificacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_tipoidentificacion (id, nombre_tipo) FROM stdin;
1	CC
2	NIT
3	TI
4	Pasaporte
5	CE
\.


--
-- Data for Name: core_usuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_usuario (id, nombre_usuario, email, password_hash, activo, token_verificacion, token_password, nuevo_email_pendiente, token_cambio_email, token_cambio_email_expiracion, rol_id) FROM stdin;
1	admin	admin@crm.com	admin123	t	\N	\N	\N	\N	\N	1
2	Jary	jaryluna07@gmail.com	LULU0713.	t		\N	\N	\N	\N	1
3	Luna	lunavale601@gmail.com	LUNA2505.	t		\N	\N	\N	\N	2
\.


--
-- Data for Name: core_contacto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_contacto (id, documento_nit, telefono, celular, direccion, ciudad, correo, nombre, apellido, fecha_expedicion, estado_civil, razon_social, nombre_rep_legal, id_rep_legal, fecha_registro, activo, historial_cambios, tipo_contacto_id, tipo_doc_id, usuario_asignado_id) FROM stdin;
2	1110471948	\N	3153048979	calle 12 carrera 45 casa 3	Medellin	Julietag@gmail.com	Julieta	Gomez	\N	\N			\N	2026-06-10 08:02:44.339748-05	t	[10/06/2026 08:02] Registrado por Jary	1	1	2
1	1110466588	\N	3214806101	calle 35 n 5-85 sur	Bogotá	Isabellatr@gmail.com	Isabella	Torres 	\N	\N	\N	\N	\N	2026-06-10 08:00:40.052036-05	t	[10/06/2026 08:00] Registrado por Luna\n[10/06/2026 08:18] Modificó Celular por Jary\n[10/06/2026 08:20] Modificó Celular por Jary\n[10/06/2026 08:35] Modificó Celular por Jary\n[10/06/2026 09:14] Modificó Celular por Jary	1	1	3
\.


--
-- Data for Name: core_tipointeraccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_tipointeraccion (id, nombre_tipo) FROM stdin;
1	Nota
2	Tarea
3	Reunión
4	Llamada
5	Correo
6	Actividad
\.


--
-- Data for Name: core_interaccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_interaccion (id, detalle_actividad, es_exitosa, procede_a_compromiso, fecha_interaccion, fecha_actualizacion, tipo_comunicacion, mensaje_id, destacado, estado, modalidad, asunto, fecha_reunion, hora_reunion, direccion, enlace_reunion, historial_cambios, duracion_minutos, temperatura_emocional, contacto_id, parent_id, canal_comunicacion_id, tipo_interaccion_id, usuario_responsable_id) FROM stdin;
1	[Información y Calificación] Información  del proyecto	f	f	2026-06-10 09:39:37.888435-05	2026-06-10 09:39:37.888443-05	Saliente	\N	f	Abierta		Diseño y construcción de casas personalizadas	\N	\N	\N	\N	[10/06/2026 09:39] Actividad iniciada por Jary	\N	\N	1	\N	\N	6	2
2	gcfuoj	f	f	2026-06-10 09:40:03.100063-05	2026-06-10 09:40:03.10007-05	Saliente	\N	f	Programada	Virtual	Aclaraciones del contrato 	2026-06-11	11:39:00	\N	https://co.pinterest.com/pin/138626494775954651/	[10/06/2026 09:40] Programada por Jary	\N	\N	1	1	3	3	2
\.


--
-- Data for Name: core_compromiso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_compromiso (id, descripcion_compromiso, estado, fecha_limite, interaccion_id) FROM stdin;
\.


--
-- Data for Name: core_firmadigital; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_firmadigital (id, html_content, pdf_attachment, usuario_id) FROM stdin;
\.


--
-- Data for Name: core_mensajewhatsapp; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.core_mensajewhatsapp (id, texto, fecha_envio, direccion, whatsapp_id, estado, contacto_id, remitente_usuario_id) FROM stdin;
1	hola.	2026-06-10 08:18:21.888426-05	Saliente	mock-287e395e-db77-429f-a362-66782f9bd5f8	enviado	1	2
2	Hola Jary, entiendo perfectamente. Vamos a revisarlo en la Constructora DYCO.	2026-06-10 08:18:21.93647-05	Entrante	mock-reply-7df71722-6cda-4de7-8d81-96a3a97c80f5	leido	1	\N
3	.	2026-06-10 08:20:47.809009-05	Saliente	mock-f42a9212-5c79-4a89-9688-6f39f2c473e0	enviado	1	2
4	Recibido. Me parece una excelente propuesta de proyecto.	2026-06-10 08:20:47.837824-05	Entrante	mock-reply-61fe62ee-ba74-40d3-abc6-b1df892af0ab	leido	1	\N
5	hola	2026-06-10 08:34:54.748413-05	Saliente	mock-9514c1c2-0ed8-4f94-8883-62bb9b0276b1	enviado	1	2
6	Recibido. Me parece una excelente propuesta de proyecto.	2026-06-10 08:34:54.767737-05	Entrante	mock-reply-4a75d734-b25d-49e9-b790-2a1a7d657d8d	leido	1	\N
7	hola	2026-06-10 08:35:33.375416-05	Saliente	mock-70ead2ca-b42d-4a8f-9bb2-5e16521f8088	enviado	1	2
8	Gracias por la información. ¿Cuándo podríamos programar una visita?	2026-06-10 08:35:33.403351-05	Entrante	mock-reply-c7195708-b5dd-4a05-9578-60f31ba3f103	leido	1	\N
9	Hola.	2026-06-10 09:14:52.055569-05	Saliente	wamid.HBgMNTczMjE0ODA2MTAxFQIAERgSMjYyNDQ2M0FDMUQyMkUwM0FCAA==	enviado	1	2
10	como estas?	2026-06-10 09:15:07.279665-05	Saliente	wamid.HBgMNTczMjE0ODA2MTAxFQIAERgSMURBN0I1QUY0NTZCQTc5MzY1AA==	enviado	1	2
\.


--
-- Name: core_compromiso_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_compromiso_id_seq', 1, false);


--
-- Name: core_contacto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_contacto_id_seq', 2, true);


--
-- Name: core_firmadigital_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_firmadigital_id_seq', 1, false);


--
-- Name: core_interaccion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_interaccion_id_seq', 2, true);


--
-- Name: core_mensajewhatsapp_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_mensajewhatsapp_id_seq', 10, true);


--
-- Name: core_rol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_rol_id_seq', 2, true);


--
-- Name: core_tipocontacto_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_tipocontacto_id_seq', 2, true);


--
-- Name: core_tipoidentificacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_tipoidentificacion_id_seq', 5, true);


--
-- Name: core_tipointeraccion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_tipointeraccion_id_seq', 6, true);


--
-- Name: core_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.core_usuario_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 3PlRHzZCZ2ckZZr6nVvlGrfdKAwfSD0b3mK12BO1mhOQT2luKkEQpKpAC8499XD

