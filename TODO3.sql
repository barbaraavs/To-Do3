CREATE TABLE Empresa
(
    EmpresaId INT NOT NULL,
    RazaoSocial VARCHAR(160) NOT NULL,
    Cnpj VARCHAR(14) NOT NULL,
    CONSTRAINT PK_Empresa PRIMARY KEY (EmpresaId)
);

CREATE TABLE Tecnologia
(
    TecnologiaId INT NOT NULL,
    "Area" VARCHAR(50) NOT NULL,
    CONSTRAINT PK_Tecnologia PRIMARY KEY (TecnologiaId)
);

CREATE TABLE Registros
(
    RegistrosId INT NOT NULL,
    TecnologiaId INT NOT NULL,
    EmpresaId INT NOT NULL,
  	CreatedAt DATE,
    CONSTRAINT PK_Registros PRIMARY KEY  (RegistrosId)
);

ALTER TABLE Registros ADD CONSTRAINT FK_RegistrosEmpresaId
    FOREIGN KEY (EmpresaId) REFERENCES Empresa (EmpresaId) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IFK_RegistrosEmpresaId ON Registros (EmpresaId);

ALTER TABLE Registros ADD CONSTRAINT FK_RegistrosTecnologia
    FOREIGN KEY (TecnologiaId) REFERENCES Tecnologia (TecnologiaId) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IFK_RegistrosTecnologiaId ON Registros (TecnologiaId);

INSERT INTO Empresa (EmpresaId,RazaoSocial,Cnpj) VALUES (1,'Renata e Rosa Eletrônica Ltda','20044903000181');
INSERT INTO Empresa (EmpresaId,RazaoSocial,Cnpj) VALUES (2,'Igor e Marcos Vinicius Telecomunicações ME', '14695719000187');
INSERT INTO Empresa (EmpresaId,RazaoSocial,Cnpj) VALUES (3,'Henrique e Malu Entulhos ME','21611097000149');
INSERT INTO Empresa (EmpresaId,RazaoSocial,Cnpj) VALUES (4,'Isabel e Ryan Transportes Ltda','24696759000119');
INSERT INTO Empresa (EmpresaId,RazaoSocial,Cnpj) VALUES (5,'Antonio e Augusto Entregas Expressas Ltda','61305963000198');

INSERT INTO Tecnologia (TecnologiaId,"Area") VALUES (1,'webdev');
INSERT INTO Tecnologia (TecnologiaId,"Area") VALUES (2,'dados');
INSERT INTO Tecnologia (TecnologiaId,"Area") VALUES (3,'marketing');
INSERT INTO Tecnologia (TecnologiaId,"Area") VALUES (4,'produto');
INSERT INTO Tecnologia (TecnologiaId,"Area") VALUES (5,'negócio');

INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (1,5,3,'01/01/2022');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (2,1,2,'01/01/2022');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (3,3,5,'01/01/2022');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (4,4,1,'01/01/2022');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (5,2,4,'01/01/2022');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (6,1,3,'01/02/2021');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (7,5,1,'01/02/2021');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (8,3,4,'01/02/2021');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (9,4,2,'01/02/2021');
INSERT INTO Registros (RegistrosId,TecnologiaId,EmpresaId,CreatedAt) VALUES (10,2,5,'01/02/2021');

--PERGUNTA 1
select 
	r.tecnologiaid,
	t."Area",
	count(distinct e.empresaid) as empresaid
from empresa as e
left join registros as r
	on r.empresaid = e.empresaid 
left join tecnologia as t 
	on t.tecnologiaid = r.tecnologiaid 
where r.createdat = '2022-01-01'
group by 1,2
order by 3 desc

--PERGUNTA 2
select 
	r.tecnologiaid,
	t."Area",
	count(distinct e.empresaid) as empresaid
from empresa as e
left join registros as r
	on r.empresaid = e.empresaid 
left join tecnologia as t 
	on t.tecnologiaid = r.tecnologiaid 
where r.createdat = '2021-02-01'
group by 1,2
order by 3 desc

--PERGUNTA 3
select 
	count(e.empresaid) as "Utilizam Dados"
from tecnologia as t
left join registros as r
	on r.tecnologiaid = t.tecnologiaid 
left join empresa as e
	on e.empresaid = r.empresaid 
where "Area" = 'dados'

--PERGUNTA 4
select 
	count(e.empresaid) as "Não Utilizam Dados"
from tecnologia as t
left join registros as r
	on r.tecnologiaid = t.tecnologiaid 
left join empresa as e
	on e.empresaid = r.empresaid 
where "Area" <> 'dados'