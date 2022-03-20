data last updated: 2022-03-16
Data source: https://main.knesset.gov.il/Activity/Info/Pages/Databases.aspx
Data flow diagram: https://gitmind.com/app/flowchart/3778623182
Repository: https://github.com/Effrat/shakuf_cooperation_in_legislation



Introduction:
=============
The goal of this project is to quantify and compare the levels of cooperation on bills sponsoring by members if the Israeli Knesset.
A 'sponsor' in this document will refer to either initiator or joiner (to the bill).
For this purpose, we define 'cooperation' as sponsoring a bill that is mostly sponsored by 'the other side' (sides: coalition / opposition), or a bill that has equal number of sponsors from each side.
While a list of connections between sponsors and bills is provided by the Knesset's database, no data is available on the association of the sponsors to a side.
Therefore, we need to create a connection between each bill to a date, and each member of Knesset to a date to a side.
Then the data can be joined on the dates, so that each association will also contain data for the side of the sponsor on the date associated with the bill.
In order to assign a side for each member of Knesset for each date, we need to assign a side for each faction for ach date.

Each bill sponsor can either be an initiator or a joiner. The bill side is defined here as the side with more initiators than the other. If the number of initiators is equal on both side, than the bill is considered to be bipartisan.



Data transformation logic:
===========================
* members_of_knesset_by_date are defined by filtering KNS_PersonToPosition on position_id field for numbers in [43, 61].
* members_of_faction_by_date are defined by filtering KNS_PersonToPosition on position_id field for numbers in [48, 54].
* people_in_government_by_date are defined by filtering KNS_PersonToPosition on position_id field for numbers in [31, 39, 40, 45, 49, 50, 51, 57, 59, 65, 73] or in [29, 30, 122, 123, 285078].



Assumptions:
============
* For each bill, the date associated with the bill is the first date the bill was scheduled to be discussed, either in a plenum session, or in a committee session.
* Bill initiators/joiners include initiators/joiners who were removed from initiators/joiners list, for various reasons.
* For each date, if a certain faction has at least 1 person "in government", then the faction is considered to be in the coalition at that date.
    -> All other active factions on that date are considered to be in the opposition.
    -> The association of members of a faction to the coalition/opposition is determined by the faction's association at that date, unless manually corrected.



Possible missing data:
======================
# TODO: For each possibility:
    - Add errors report to main report
    - need to decide whether to: (1) add missing data, (2) drop row or (3) leave as is

-> Member of Knesset data is missing for a certain date
    #TODO: define & add missing data to members_of_knesset_by_date
    - will appear as less then 120 members in the Knesset, for each relevant date in members_of_knesset_by_date
    missing data to bo added in:

-> Member of faction data is missing for a certain date
    #TODO: define & add missing data to members_of_faction_by_date
    - will appear as a member of Knesset w/o faction and side, for each relevant date in members_of_knesset_faction_by_date
    missing data to bo added in:

-> People in government data is missing for a certain date (people_in_government_by_date)
    #TODO: define & add missing data to people_in_government_by_date
    - could appear a faction in opposition instead of coalition for certain dates in faction_side_by_date
    - external knowledge is needed to determine if data is missing
    missing data to bo added in:

-> Faction in coalition, but not in Knesset by date
    - automatic report created by faction_side_by_date in reports folder: factions_in_coalition_not_in_knesset_by_date.csv
    #TODO: report must be empty
    missing data to bo added in:

-> People in government w/o faction data for date
    - automatic report created by faction_side_by_date in reports folder: people_in_government_wo_faction_by_date.csv
    #TODO: report must be empty
    missing data to bo added in:

-> First session w/ discussion over bill w/o date data
    - automatic reports created by bill_to_date_from_session & bill_to_date_from_committee_session
        in reports folder: nan_dates_from_session.csv, nan_dates_from_committee_session.csv
    #TODO: reports must be empty
    missing data to bo added in: bill_to_date_from_session, bill_to_date_from_committee_session

-> Bills discussed (either in committee or plenum) w/ missing sponsors data
    - rows are dropped by inner join in all_bill_sponsors_to_date ---v
    - report created by all_bill_sponsors_to_date in reports folder: bills_w_date_wo_sponsors.csv ---v

 -> Bills w/ sponsors data w/o date
    - rows are dropped by inner join in all_bill_sponsors_to_date ---v
    - report created by all_bill_sponsors_to_date in reports folder: bills_w_sponsors_wo_dates.csv ---v







-> Members of faction who are not Members of Knesset for date (members_of_knesset_faction_by_date, knesset_num == NaN, filtered in PowerBI's back-end) ---v
-> Member of Knesset w/o faction data for date (members_of_knesset_faction_by_date) #TODO: manually fill NaNs in faction_id
-> Sponsor w/o faction data for date (bill_sponsors, faction_id == NaN) #TODO: manually fill NaNs in faction_id or drop
-> Member of Knesset w/ faction data, w/o bill data (bill_sponsors, faction_id != NaN & bill_id == NaN) #TODO: filter in PowerBI's back-end
-> Bill w/o sponsors data (bill, knesset_num from KNS_Bill != NaN & knesset_num from KNS_PersonToPosition == NaN)
-> Bill w/o name data (bill, name == "")

* Data for most recent dates might not be updated (der'i, current Knesset/government) #TODO: manually add missing data



Contact:
========
To report bugs or missing data, please contact me at: effratk@gmail.com