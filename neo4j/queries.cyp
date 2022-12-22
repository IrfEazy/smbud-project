MATCH(n)
DETACH DELETE n;

CALL apoc.load.json('dataset.json') YIELD value;

CREATE (p:Paper {id:       value._id,
                 title:    value.title,
                 year:     value.year,
                 lang:     value.lang,
                 doi:      value.doi,
                 url:      value.url,
                 abstract: value.abstract})
WITH p, value
UNWIND value.keywords AS kw
WITH p, value, kw
  WHERE kw IS NOT NULL
MERGE (k:Keyword {keyword: kw})
MERGE (p)-[h:HIGHLIGHTS]->(k)
WITH p, value
UNWIND value.fos AS fos
WITH p, value, fos
  WHERE fos IS NOT NULL
MATCH (p:Paper {id: value._id})
MERGE (f:Fos {fos: fos})
MERGE (p)-[b:BELONGS_TO]->(f);

UNWIND value.authors AS aut
WITH aut, value
  WHERE aut._id IS NOT NULL AND aut.name IS NOT NULL
MERGE (a:Author {id:   aut._id,
                 name: aut.name})
WITH a, aut, value
MATCH (p:Paper {id: value._id})
CREATE (a)-[w:WRITES {affiliation: aut.org}]->(p);

UNWIND value.venue AS ven
WITH value, ven
  WHERE value.publication_type = 'Book'
CREATE (b:Publication:Book {isbn:      value.isbn,
                            publisher: value.publisher,
                            name:      ven.raw})
WITH b, value
MATCH (p:Paper {id: value._id})
CREATE (p)-[i:IS_PART_OF {page_start: toInteger(value.page_start),
                          page_end:   toInteger(value.page_end)}]->(b);

UNWIND value.venue AS ven
WITH value, ven
  WHERE value.publication_type = 'Conference'
CREATE (c:Publication:Conference {name:     ven.raw,
                                  location: value.location})
WITH c, value
MATCH (p:Paper {id: value._id})
CREATE (p)-[i:IS_PART_OF {page_start: toInteger(value.page_start),
                          page_end:   toInteger(value.page_end)}]->(c);

UNWIND value.venue AS ven
WITH value, ven
  WHERE value.publication_type = 'Journal'
CREATE(j:Publication:Journal {issn:      value.issn,
                              publisher: value.publisher,
                              name:      ven.raw,
                              volume:    value.volume,
                              issue:     value.issue})
WITH j, value
MATCH (p:Paper {id: value._id})
CREATE (p)-[i:IS_PART_OF {page_start: toInteger(value.page_start),
                          page_end:   toInteger(value.page_end)}]->(j);

UNWIND value.references AS ref
WITH value, ref
  WHERE ref IS NOT NULL
MATCH (a:Paper {id: value._id})
MATCH (b:Paper {id: ref})
MERGE (a)-[r:REFERENCES]->(b);

MATCH (a:Author {id:   '53f463b3dabfaee4dc8430d5',
                 name: 'Annabel Sebag'})
MERGE (new_p:Paper {doi:        '10.1145/1596685.1596829',
                    id:         '53e997cbb7602d9701fbcee3',
                    title:      'Yankee gal',
                    year:       2009,
                    lang:       'en',
                    page_start: 155,
                    page_end:   155,
                    url:        ['https://dx.doi.org/10.1145/1596685.1596829',
                                  'https://doi.acm.org/10.1145/1596685.1596829',
                                  'db/conf/siggraph/siggraph2009festival.html#Sebag09c',
                                  'https://doi.org/10.1145/1596685.1596829'],
                    abstract:   'This is a graduate film from the students of Supinfocom Valenciennes.'})
MERGE aff = (a)-[:WRITES {affiliation: '53f463b3dabfaee4dc8430d5'}]->(new_p)
MERGE f2 = (new_p)-[:BELONGS_TO]->(:Fos {fos: 'siggraph'})
MERGE k1 = (new_p)-[:HIGHLIGHTS]->(kw1:Keyword {keyword: 'yankee gal'})
MERGE k2 = (new_p)-[:HIGHLIGHTS]->(kw2:Keyword {keyword: 'supinfocom valenciennes'})
MERGE k3 = (new_p)-[:HIGHLIGHTS]->(kw3:Keyword {keyword: 'graduatethe query aims"animation'})
RETURN aff, f1, f2, k1, k2, k3;

MATCH (a:Author {name: 'James Ostell'}), (np:Paper {title: 'Grow'})
MERGE res = (a)-[:WRITES {affiliation: 'Federal Institute of Technology, Switzerland'}]->(np)
RETURN res;

MATCH (p:Publication)
  WHERE p.isbn IS NOT NULL
SET p:Book
RETURN p;

MATCH (paper:Paper)-[i:IS_PART_OF]->(:Book)
  WHERE paper.id = '53e99785b7602d9701f40556'
SET i.page_start = 15
SET i.page_end = 33;

MATCH (:Paper)-[i:IS_PART_OF]->(:Book)
  WHERE i.page_start < 0
REMOVE i.page_start;

MATCH (:Paper)-[i:IS_PART_OF]->(:Book)
  WHERE i.page_end < 0
REMOVE i.page_end;

MATCH (:Paper)-[i:IS_PART_OF]->(:Book)
  WHERE NOT i.page_start IS NULL AND NOT i.page_end IS NULL AND i.page_end - i.page_start < 0
REMOVE i.page_start, i.page_end;

MATCH (b:Book {name: 'Mathematics and Computers in Simulation'})
DETACH DELETE b;

MATCH g = (:Author)-[:WRITES]->(:Paper {title: 'CodeTalk'})
RETURN g;

MATCH (:Author {name: 'Annabel Sebag'})-[r:WRITES]-(p:Paper)
WITH r.affiliation AS affiliation, p.year AS year
  ORDER BY year DESC
RETURN DISTINCT affiliation, year;

MATCH (a:Author)-[:WRITES]->(p:Paper)-[:IS_PART_OF]->(j:Journal)
  WHERE p.year = 2005 AND j.name = 'Briefings in Bioinformatics'
RETURN DISTINCT a.name AS authorName;

MATCH (:Author)-[:WRITES {affiliation: 'Wien'}]->(:Paper)-[:IS_PART_OF]->(b:Journal)
RETURN DISTINCT b.name AS journalName;

MATCH (a:Author)-[:WRITES]->(p:Paper)-[:IS_PART_OF]->(:Journal)
  WHERE p.year = 2000
WITH a, COUNT(*) AS paperNum
RETURN a.name AS authorName, paperNum
  ORDER BY paperNum DESC
  LIMIT 5;

MATCH (a:Author)-[:WRITES]->(p:Paper)-[:IS_PART_OF]->(c:Conference)
  WHERE a.name STARTS WITH 'A' OR a.name STARTS WITH 'S'
WITH c.name AS conference, c.location AS location, count(DISTINCT p) AS number_of_papers
RETURN DISTINCT conference, location, number_of_papers
  ORDER BY number_of_papers DESC
  LIMIT 5;

MATCH (a:Author)-[w:WRITES]->(:Paper)<-[r:REFERENCES]-(:Paper)-[:IS_PART_OF]->(:Book)
  WHERE w.affiliation = 'University of Mannheim'
WITH a, count(DISTINCT r) AS totalReferences
  WHERE totalReferences > 2
RETURN a.name AS authorName, totalReferences;

MATCH (a1:Paper)-[:REFERENCES*3..6]->(a2:Paper)
  WHERE id(a1) <> id(a2)
RETURN DISTINCT a1.title AS firstPaper, a2.title AS secondPaper
  LIMIT 5;

MATCH (a1:Paper)-[:REFERENCES]->(a2:Paper)-[:REFERENCES]->(a3:Paper)-[:REFERENCES]->(a4:Paper)-[:REFERENCES]->(a5:Paper)
        -[:REFERENCES]->(a6:Paper)
  WHERE id(a1) <> id(a2) AND id(a2) <> id(a3) AND id(a3) <> id(a4) AND id(a4) <> id(a5) AND id(a5) <> id(a6)
RETURN DISTINCT a1.title AS firstPaper, a6.title AS secondPaper
  LIMIT 5;

MATCH (a:Author)-[:WRITES]->(p:Paper)<-[:WRITES]-(ca:Author), (p)-[:IS_PART_OF]->(:Journal)
WITH DISTINCT a, ca, count(DISTINCT p) AS cnt
  ORDER BY cnt DESC
WITH DISTINCT a, collect(ca.name) AS colabs, collect(cnt) AS cnts
RETURN a.name AS author, colabs[0] AS bestCollaborator, cnts[0] AS numberOfPapers
  LIMIT 5;

MATCH (founder:Paper)-[:BELONGS_TO]->(fos:Fos {fos: 'Statistics'})<-[:BELONGS_TO]-(p:Paper)
  WHERE id(founder) <> id(p)
WITH collect(p) AS test, founder, fos
  WHERE ALL(p IN test
    WHERE NOT exists((founder)-[:REFERENCES*7]->(p)))
RETURN fos AS field, collect(DISTINCT founder.title) AS founderPapers;

MATCH(a:Author)-[w:WRITES {affiliation: 'Federal Institute of Technology, Switzerland'}]->(p:Paper)
       -[i:IS_PART_OF]->(j:Journal)
  WHERE i.page_start IS NOT NULL AND i.page_end IS NOT NULL
WITH a, sum(i.page_end - i.page_start) AS num_pag
  ORDER BY num_pag DESC
RETURN a AS Author, num_pag;

MATCH (a1:Author)-[w1:WRITES]->(p1:Paper)-[:IS_PART_OF]->(j:Journal {name: 'Commun. ACM'}),
      (p1:Paper)-[:BELONGS_TO]->(fos:Fos),
      (a2:Author)-[w2:WRITES]-(p1:Paper)
  WHERE a1 <> a2 AND w1.affiliation IS NOT NULL
WITH w1.affiliation AS affiliation, collect(DISTINCT fos) AS fieldsOfStudy, collect(DISTINCT w2.affiliation) AS others,
     count(DISTINCT p1) AS numberOfPapers
  WHERE ALL(organization IN others
    WHERE affiliation = organization)
WITH affiliation, fieldsOfStudy, numberOfPapers
  ORDER BY numberOfPapers DESC
RETURN affiliation, fieldsOfStudy, numberOfPapers
  LIMIT 2;

MATCH (p1:Paper)-[:IS_PART_OF]->(b1:Book),
      (p1:Paper)-[:BELONGS_TO]->(fos1:Fos)<-[:BELONGS_TO]-(p2:Paper),
      (p1)-[:HIGHLIGHTS]->(k1:Keyword)<-[:HIGHLIGHTS]-(p2),
      (p2:Paper)-[:IS_PART_OF]->(b2:Book)
  WHERE b1 <> b2 AND p1 <> p2 AND b1.name = 'RoboCup 2009'
WITH b1, b2, collect(DISTINCT fos1) AS fos, count(DISTINCT k1) AS score
  ORDER BY score DESC
RETURN b2.name AS relatedBook, fos, score
  LIMIT 3;

MATCH (a1:Author)-[w1:WRITES]->(p1:Paper)<-[w2:WRITES]-(a2:Author),
      (a2:Author)-[w3:WRITES]->(p2:Paper)<-[w4:WRITES]-(a3:Author),
      (a1)-[:WRITES]->(p3:Paper)-[:BELONGS_TO]->(f1:Fos)<-[:BELONGS_TO]-(p4:Paper)<-[:WRITES]-(a3)
  WHERE NOT exists ((a1)-[:WRITES]->(:Paper)<-[:WRITES]-(a3)) AND a1 <> a3 AND a1 <> a2 AND a2 <> a3
WITH a1, a3, collect(DISTINCT f1.fos) AS fields, count(DISTINCT f1) AS common_fields,
     count(DISTINCT p1) AS common_collabs1, count(DISTINCT p2) AS common_collabs2
  WHERE common_collabs1 > 1 AND common_collabs2 > 1
WITH a1, a3, fields, common_fields, common_collabs1 + common_collabs2 AS common_collabs
  ORDER BY common_fields DESC, common_collabs DESC
RETURN DISTINCT a1.name AS Author1, a3.name AS Author2, fields, common_collabs, common_fields
  LIMIT 5;

MATCH (fos1:Fos)<-[:BELONGS_TO]-(p1:Paper) -[:BELONGS_TO]->(:Fos {fos: 'Irrigation'}),
      (fos2:Fos)<-[:BELONGS_TO]-(p2:Paper) -[:BELONGS_TO]->(:Fos {fos: 'Artificial intelligence'})
  WHERE p1 <> p2
WITH p1, collect(DISTINCT fos1) AS foss1, p2, collect(DISTINCT fos2) AS foss2
  WHERE ALL(f IN foss1
    WHERE NOT f IN foss2)
MATCH sp = shortestPath((p1)-[:REFERENCES*..7]->(p2))
  WHERE length(sp) > 1
RETURN sp
  LIMIT 1;
