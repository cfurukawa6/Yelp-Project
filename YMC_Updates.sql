update Business2
set numcheckins = B.numchecks from
(select b.busID, b.name, sum(c.numCheck) as numchecks
 from Business2 as b inner join Checkin as c on b.busID = c.busID
 group by b.busID, b.name) as B where Business2.busID = B.busID

update Business2
set numreviews = B.reviewCount from
(select b.busID, b.name, count(r.reviewID) as reviewCount
  from Business2 as b inner join Review as r on b.busID = r.busID
  group by b.busID, b.name) as B where Business2.busID = B.busID

update Business2
set avgrating = B.average from
(select b.busID, b.name, sum(cast(r.Stars as float))/count(cast(r.stars as float)) as average
  from Business2 as b inner join Review as r on b.busID = r.busID
  group by b.busID, b.name) as B where Business2.busID = B.busID
