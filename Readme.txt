last update: 2022-03-15



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