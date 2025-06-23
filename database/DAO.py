from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAlbums(dMin):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""select a.*, sum(t.Milliseconds)/1000/60 as dTot
from album a, track t
where a.AlbumId= t.AlbumId
group by a.AlbumId
having dTot > %s
        """
        cursor.execute(query, (dMin,)) #in minuti
        res=[]
        for row in cursor:
            res.append(Album(**row))
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllEdges(idMap):
            cnx = DBConnect.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """select DISTINCTROW  t1.AlbumId as a1,t2.AlbumId as a2
from track t1, track t2, playlisttrack p1,playlisttrack p2
where t2.TrackId= p2.TrackId
and t1.TrackId=p1.TrackId
and p2.PlaylistId=p1.PlaylistId
and t1.AlbumId < t2.AlbumId 

            """
            cursor.execute(query)  # in minuti
            res = []
            for row in cursor:
                if row["a1"] in idMap and row["a2"] in idMap:
                    res.append((idMap[row["a1"]], idMap[row["a2"]]))
            cursor.close()
            cnx.close()
            return res


