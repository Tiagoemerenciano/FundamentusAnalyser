CREATE SCHEMA fundamentos AUTHORIZATION postgres;

CREATE TYPE fundamentos."_fundamentos" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = fundamentos.fundamentos,
	DELIMITER = ',');

CREATE TYPE fundamentos."_papeis" (
	INPUT = array_in,
	OUTPUT = array_out,
	RECEIVE = array_recv,
	SEND = array_send,
	ANALYZE = array_typanalyze,
	ALIGNMENT = 8,
	STORAGE = any,
	CATEGORY = A,
	ELEMENT = fundamentos.papeis,
	DELIMITER = ',');

CREATE TYPE fundamentos.fundamentos AS (
	id uuid,
	papel varchar,
	preco_por_lucro float8,
	preco_por_valorpatrimonial float8,
	psr float8,
	dividend_yield float8,
	preco_por_ativos float8,
	preco_por_capitaldegiro float8,
	preco_por_ativocirculanteliquido float8,
	preco_por_ebit float8,
	ev_por_ebit float8,
	ev_por_ebitda float8,
	margem_ebit float8,
	margem_liquida float8,
	liquidez_corrente float8,
	roic float8,
	roe float8,
	liquidez_dois_meses float8,
	divida_bruta_por_patrimonio float8,
	crescimento_receita_cinco_anos float8,
	data_alteracao timestamp,
	patrimonio_liquido float8);

CREATE TYPE fundamentos.papeis AS (
	codigo varchar,
	empresa varchar);

CREATE TABLE fundamentos.papeis (
	codigo varchar NOT NULL,
	empresa varchar NULL,
	CONSTRAINT papeis_pk PRIMARY KEY (codigo)
);

CREATE TABLE fundamentos.fundamentos (
	id uuid NOT NULL DEFAULT gen_random_uuid(),
	papel varchar NULL,
	preco_por_lucro float8 NULL,
	preco_por_valorpatrimonial float8 NULL,
	psr float8 NULL,
	dividend_yield float8 NULL,
	preco_por_ativos float8 NULL,
	preco_por_capitaldegiro float8 NULL,
	preco_por_ativocirculanteliquido float8 NULL,
	preco_por_ebit float8 NULL,
	ev_por_ebit float8 NULL,
	ev_por_ebitda float8 NULL,
	margem_ebit float8 NULL,
	margem_liquida float8 NULL,
	liquidez_corrente float8 NULL,
	roic float8 NULL,
	roe float8 NULL,
	liquidez_dois_meses float8 NULL,
	divida_bruta_por_patrimonio float8 NULL,
	crescimento_receita_cinco_anos float8 NULL,
	data_alteracao timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	patrimonio_liquido float8 NULL,
	CONSTRAINT fundamentos_pk PRIMARY KEY (id),
	CONSTRAINT fundamentos_un UNIQUE (papel),
	CONSTRAINT fundamentos_fk FOREIGN KEY (papel) REFERENCES fundamentos.papeis(codigo)
);
