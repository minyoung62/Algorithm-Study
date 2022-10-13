select i.animal_id, i.animal_type, i.name
from animal_ins as i
join animal_outs as o
on i.animal_id = o.animal_id
where i.sex_upon_intake like 'Intact %' 
and (o.sex_upon_outcome like 'Spayed %'
or o.sex_upon_outcome like 'Neutered %')
 











# -- 코드를 입력하세요
# SELECT o.animal_id, o.animal_type , o.name
# from animal_outs as o
# join animal_ins as i
# on o.animal_id = i.animal_id
# where i.sex_upon_intake like "Intact %" 
# and o.sex_upon_outcome not like "Intact %"