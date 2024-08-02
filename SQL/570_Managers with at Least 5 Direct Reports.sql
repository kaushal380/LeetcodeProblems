select name from employee a join (
select managerId from Employee group by managerId Having count(*) >= 5) b on a.id = b.managerId;
