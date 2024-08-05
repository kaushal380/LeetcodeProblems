--Difficulty : easy

select u.unique_id, E.name from Employees E left join EmployeeUNI U  on E.id = U.id
