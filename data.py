from rk1.browser import BR
from rk1.computer import PK
from rk1.brows_and_pk import PKBR


brs = [
    BR(1,'Opera'),
    BR(2,'FireFox'),
    BR(3,'DuckDuckGo'),
    BR(4,'Google'),
    BR(5,'Yandex'),
    BR(6,'MS Edge')
]

pks = [
    PK(1,25000,'Russia',2),
    PK(2,50000,'Roma',6),
    PK(3,67500,'China',2),
    PK(4,60000,'USA',3),
    PK(5,50000,'China',4),
    PK(6,167500,'USA',4),
    PK(7,225000,'China',6),
    PK(8,70000,'USA',2),
    PK(9,627500,'China',5),
    PK(10,251000,'USA',5),
    PK(11,54000,'China',5),
    PK(12,672500,'China',1),
    PK(13,250000,'USA',1),
    PK(14,500000,'China',3),
    PK(15,62330,'China',4)
]

pkbrs = [
    PKBR(1,2),
    PKBR(2,2),
    PKBR(3,5),
    PKBR(4,2),
    PKBR(5,5),
    PKBR(6,3),
    PKBR(7,1),
    PKBR(8,4),
    PKBR(9,6),
    PKBR(10,6)
]

"""Основная функция"""
one_to_many = [(br.name, pk.cost, pk.made_in)
    for br in brs
    for pk in pks
    if pk.id_br == br.id_br]

many_to_many_temp = [(br.name, pbs.id_br, pbs.id_pk)
    for br in brs
    for pbs in pkbrs
    if br.id_br==pbs.id_br]

many_to_many = [(pk.cost, pk.made_in, br_name)
    for br_name, br_id, pk_id in many_to_many_temp
    for pk in pks
    if pk_id == pk.id_pk]
    