ClassroomHelper Project 18.02.2017


Content of the DataBase for testing

All records from 'module' table
(1, 'M01001', 'Art of nothing', 'Nobody helped me out, so no description, you write better if you want')
(2, 'M01003', 'How to tip a cow', 'Nobody helped me out, so no description, you write better if you want')
(3, 'M02001', 'Chololate unwrapping Studies', 'Nobody helped me out, so no description, you write better if you want')
(4, 'M03001', 'How to oreder at McD. efficiently', 'Nobody helped me out, so no description, you write better if you want')
(5, 'M03010', "Spliff Rollin' Course", 'Nobody helped me out, so no description, you write better if you want')
(6, 'M03011', 'Do WHATEVER professionally', 'Nobody helped me out, so no description, you write better if you want')

All records from 'student' table
(1, '17159114703', '', 'Loretta', 'Staley', '14/03/1997', 'p@ssword')
(2, '17149326610', '', 'Nilsa', 'Govea', '26/10/1989', 'p@ssword')
(3, '17144625309', '', 'Elaina', 'Kennell', '25/09/2000', 'p@ssword')
(4, '17144204304', '', 'Leandro', 'Direnzo', '04/04/1994', 'p@ssword')
(5, '17151825204', '', 'Elaina', 'Robnett', '25/04/1999', 'p@ssword')
(6, '17146913010', '', 'Kiera', 'Gamache', '13/10/1996', 'p@ssword')
(7, '17161920310', '', 'Versie', 'Kennell', '20/10/1998', 'p@ssword')
(8, '17144314904', '', 'Edmundo', 'Kennell', '14/04/1991', 'p@ssword')
(9, '17144225009', '', 'Demarcus', 'Leigh', '25/09/2000', 'p@ssword')
(10, '17160226210', '', 'Refugio', 'Nuno', '26/10/1989', 'p@ssword')
(11, '17145725904', '', 'Estela', 'Leigh', '25/04/1999', 'p@ssword')
(12, '17151518704', '', 'Loretta', 'Kwok', '18/04/1990', 'p@ssword')
(13, '17151025709', '', 'Kris', 'Lauder', '25/09/2000', 'p@ssword')
(14, '17153414103', '', 'Kris', 'Neu', '14/03/1997', 'p@ssword')
(15, '17150218501', '', 'Refugio', 'Direnzo', '18/01/1997', 'p@ssword')
(16, '17144614903', '', 'Keely', 'Eddy', '14/03/1997', 'p@ssword')
(17, '17154002711', '', 'Gwenda', 'Staley', '02/11/1992', 'p@ssword')
(18, '17149904304', '', 'Gordon', 'Neu', '04/04/1994', 'p@ssword')
(19, '17156702110', '', 'Nilsa', 'Nuno', '02/10/1996', 'p@ssword')
(20, '17154507202', '', 'Shae', 'Gamache', '07/02/2000', 'p@ssword')
(21, '17153811308', '', 'Neda', 'Kueter', '11/08/1997', 'p@ssword')

All records from 'teacher' table
(1, 'st147707702', '', 'Nilsa', 'Eddy', 'p@ssword')
(2, 'st147020110', '', 'Loretta', 'Gamache', 'p@ssword')
(3, 'st164607302', '', 'Refugio', 'Robnett', 'p@ssword')
(4, 'st144605707', '', 'Conrad', 'Munsey', 'p@ssword')
(5, 'st144228203', '', 'Estela', 'Kennell', 'p@ssword')
(6, 'st147914103', '', 'Estela', 'Nuno', 'p@ssword')
(7, 'st140818703', '', 'Gordon', 'Eichhorn', 'p@ssword')

All records from 'teachedby' table
(2017, 1, 'st144228203', 'M01001')
(2017, 1, 'st140818703', 'M02001')
(2017, 1, 'st144228203', 'M03001')
(2017, 1, 'st147914103', 'M03011')
(2017, 1, 'st147020110', 'M02001')
(2017, 1, 'st164607302', 'M03001')
(2017, 1, 'st144605707', 'M03001')

All records from 'grade' table
(48, 2017, 2, '17145725904', 'M03011')
(57, 2017, 1, '17151825204', 'M03010')
(65, 2017, 1, '17144614903', 'M03010')
(67, 2017, 2, '17151025709', 'M02001')
(52, 2017, 2, '17144314904', 'M03010')
(84, 2017, 1, '17153811308', 'M03001')
(42, 2017, 2, '17144625309', 'M03010')

Sample raw output:
[(48, 2017, 2, '17145725904', 'M03011'), (57, 2017, 1, '17151825204', 'M03010'), (65, 2017, 1, '17144614903', 'M03010'), (67, 2017, 2, '17151025709', 'M02001'), (52, 2017, 2, '17144314904', 'M03010'), (84, 2017, 1, '17153811308', 'M03001'), (42, 2017, 2, '17144625309', 'M03010')]

therefore a multi value / multi row query will give you the data in the format: 
	list[ tuple1(v1,v2,v3... vn), tuple2(v1,v2,v3... vn),... tupleN(v1,v2,v3... vn)]

it is possible to get back only a single field, also same field from multiple rows (column)
eg. get back a single value of 'grade' for one specific student only,
or get back the grade for evey student in a module to calculate the overall average.





