select * from fiscal.tb_rap;

Select distinct(rap.portoorigem), count(rap.portoorigem)
from fiscal.tb_rap rap
group by rap.portoorigem;

Select distinct(rap.portodestino), count(rap.portodestino)
from fiscal.tb_rap rap
group by rap.portodestino;

Select * from fiscal.tb_portos
where nome like '%JIZAN%';