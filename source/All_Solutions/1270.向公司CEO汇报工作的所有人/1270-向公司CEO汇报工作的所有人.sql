# Write your MySQL query statement below
    (select employee_id EMPLOYEE_ID/*��һ��*/
    from Employees e 
    where manager_id=1 and employee_id!=1)
union
    (select e1.employee_id/*�ڶ���*/
    from
        (select employee_id
        from Employees e 
        where manager_id=1 and employee_id!=1)t1 
    join Employees e1 on t1.employee_id=e1.manager_id)
union/*������*/
    select e2.employee_id
    from
        (select e1.employee_id
        from
            (select employee_id
            from Employees e 
            where manager_id=1 and employee_id!=1)t1 
        join Employees e1 on t1.employee_id=e1.manager_id) t2 join Employees e2
    on t2.employee_id =e2.manager_id
order by EMPLOYEE_ID
