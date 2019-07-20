#  /usr/bin/python3.7
#
#   Author: Virgil Hoover
#   License found in './License.txt'


def network_select_query():
    sql_query = 'SELECT network.SiteID, network.Node, requests.Name, network.State, network.DateRcvd FROM network ' \
                'INNER JOIN requests ON network.RequestType = requests.ID WHERE LastAttempt IS NOT NULL'
    return sql_query


def update_network_query():
    sql_query = 'UPDATE network Set LastAttempt = CURDATE() WHERE LastAttempt IS NOT NULL'
    return sql_query


def update_server_query():
    sql_query = 'UPDATE server Set LastAttempt = CURDATE() WHERE LastAttempt IS NOT NULL'
    return sql_query


def select_server_query():
    sql_query = 'SELECT server.HostName, server.Address, requests.Name, server.DateRcvd FROM server INNER ' \
                'JOIN requests ON server.RequestType = requests.ID WHERE LastAttempt IS NOT NULL'
    return sql_query


def show_resolved_query():
    sql_query = 'SELECT (SELECT COUNT(*) FROM network WHERE yearweek(DATE(DateEntered), 1) = yearweek(curdate(), 1))' \
                ' AS Network, (SELECT COUNT(*) FROM server WHERE yearweek(DATE(DateEntered), 1) = ' \
                'yearweek(curdate(), 1)) AS Server, (SELECT COUNT(*) FROM downtime WHERE yearweek(DATE(DateComplete),' \
                ' 1) = yearweek(curdate(), 1)) AS Downtime'
    return sql_query


def select_tech_query():
    sql_query = 'SELECT Name FROM tech WHERE Active = 1;'
    return sql_query


def select_request_types_query():
    sql_query = 'SELECT Name, ID FROM requests ORDER BY ID;'
    return sql_query


def network_insert_query():
    sql_query = 'INSERT INTO network (ID, SiteID, Node, Requested, Poller, Tech, DateRcvd, DateEntered, Resolved, ' \
                'LastAttempt, RequestType, State) VALUES (NULL, '
    return sql_query


def server_insert_query():
    sql_query = 'INSERT INTO server (ID, HostName, Address, Poller, Tech, DateRcvd, DateEntered, Resolved, ' \
                'LastAttempt, RequestType, Notes, TaskNum, TicketNum) VALUES (NULL, '
    return sql_query


def downtime_insert_query():
    sql_query = 'INSERT INTO downtime (ID, Requestor, DateRequested, Completed, Request, RequestDate, Duration, ' \
                'Time, Node, WPM, Tech, Notes) VALUES (NULL, '
    return sql_query


def search_site_history_query(site_id):
    sql_query = f'SELECT network.SiteID, network.Node, requests.Name, network.State, network.DateRcvd FROM network ' \
                f'INNER JOIN requests ON network.RequestType = requests.ID WHERE network.SiteID = {site_id}'
    return sql_query


def search_network_history_query(limit):
    sql_query = f'SELECT network.SiteID, network.Node, requests.Name As RequestType, network.State, network.DateRcvd,' \
                f' network.Resolved FROM network INNER JOIN requests ON network.RequestType = requests.ID ORDER BY ' \
                f'network.DateRcvd DESC LIMIT {limit}'
    return sql_query


def search_server_history_query(limit):
    sql_query = f'SELECT server.HostName, server.Address, requests.Name As RequestType, server.DateRcvd,' \
                f' server.Resolved FROM server INNER JOIN requests ON server.RequestType = requests.ID ORDER BY ' \
                f'server.DateRcvd DESC LIMIT {limit}'
    return sql_query


def search_downtime_history_query(limit):
    sql_query = f'SELECT Request, DateRequested, Requestor, RequestDate, Time, Duration FROM downtime ORDER BY ' \
                f'DateRequested DESC LIMIT {limit};'
    return sql_query


def get_tech_id_query():
    sql_query = 'SELECT TechID FROM tech WHERE Name = '
    return sql_query


def network_update_query():
    sql_query = 'UPDATE network SET '
    return sql_query


def server_update_query():
    sql_query = 'UPDATE server SET '
    return sql_query
