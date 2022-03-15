last update: 2022-03-15


Data source:
============



Premise:
========
The goal of this project is to quantify and compare the levels of cooperation on bills sponsoring by members if the Israeli Knesset.
A 'sponsor' in this document will refer to either initiator or joiner (to the bill).
For this purpose, we define 'cooperation' as sponsoring a bill that is mostly sponsored by 'the other side' (sides: coalition / opposition), or a bill that has equal number of sponsors from each side.
While a list of connections between sponsors and bills is provided by the Knesset's database, no data is available on the association of the sponsors to a side.
Therefore, we need to create a connection between each bill to a date, and each member of Knesset to a date to a side.
Then the data can be joined on the dates, so that each association will also contain data for the side of the sponsor on the date associated with the bill.
In order to assign a side for each member of Knesset for each date, we need to assign a side for each faction for ach date.


Assumptions:
============
* For each bill, the date associated with the bill is the first date the bill was scheduled to be discussed, either in a plenum session, or in a committee session.
* Bill initiators/joiners include initiators/joiners who were removed from initiators/joiners list, for various reasons.
* For each date, if a certain faction has at least 1 person "in government", then the faction is considered to be in the coalition at that date.
    -> All other active factions on that date are considered to be in the opposition.
    -> The association of members of a faction to the coalition/opposition is determined by the faction's association at that date, unless manually corrected.


Data transformation logic:
===========================
* members_of_knesset_by_date are defined by filtering KNS_PersonToPosition on position_id field for numbers in [43, 61].
* members_of_faction_by_date are defined by filtering KNS_PersonToPosition on position_id field for numbers in [48, 54].
* people_in_government_by_date are defined by filtering KNS_PersonToPosition on position_id field for numbers in [31, 39, 40, 45, 49, 50, 51, 57, 59, 65, 73] or in [29, 30, 122, 123, 285078].




Possible missing data:
======================
* Data for most recent dates might not be updated.
* 



Additions to original data:
===========================




Contact:
========
To report bugs or missing data, please contact: effratk@gmail.com