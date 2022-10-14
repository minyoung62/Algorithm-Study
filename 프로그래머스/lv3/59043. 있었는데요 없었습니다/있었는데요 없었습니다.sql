select i.animal_id, i.name 
from animal_ins as i
join animal_outs as o
on i.animal_id = o.animal_id
where i.datetime > o.datetime
order by i.datetime

# SELECT 
# ins.animal_id, ins.name -- , ins.datetime, outs.datetime, datediff(ins.datetime, outs.datetime)
# from animal_ins as ins
# inner join animal_outs as outs on ins.animal_id = outs.animal_id
# where datediff(outs.datetime, ins.datetime) < 0
# order by ins.datetime;
