DROP TABLE IF EXISTS [DjgLeoApp001_country];
CREATE TABLE [DjgLeoApp001_country]([rowid] integer, [id] integer, [Abbr] varchar(2), [telephoneext] varchar(4), [Name] varchar(50));

INSERT INTO [DjgLeoApp001_country]([rowid], [id], [Abbr], [telephoneext], [Name])
VALUES(1, 1, 'GR', '0030', 'Ελλάδα');

INSERT INTO [DjgLeoApp001_country]([rowid], [id], [Abbr], [telephoneext], [Name])
VALUES(2, 2, 'FR', '0033', 'Γαλλία');

