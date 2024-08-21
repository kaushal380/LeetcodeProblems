select name, bonus from Employee left join Bonus on Employee.empID = Bonus.empID
where bonus is null or bonus < 1000;
