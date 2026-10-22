CREATE DATABASE practicedb;
USE practicedb;
CREATE TABLE payment_table(
Payment int ,
Customer_name VARCHAR(45),
Mode_ VARCHAR(44),
City VARCHAR(53) 
);

INSERT INTO payment_table
(Payment,Customer_name,Mode_,City)
VALUES
(101,"IKRAM ALI","netbanking","poland"),
(102,"ALI","credit card","india"),
(103,"Imaya","credit card","russia"),
(104,"kiI","netbanking","sioam"),
(105,"manish","credit card","denmer"),
(106,"IKRAM ALI","debit card","poland"),
(107,"IKRAM ALI","debit card","poland"),
(108,"amisnd","debit card","utao"),
(109,"laaba","netbanking","america"),
(110,"jackmaa","credit card","booqlt");

SELECT * FROM payment_table;
SELECT Customer_name ,Payment , MAX(Mode_)
FROM payment_table
GROUP BY Customer_name,Payment
;