/* one-time */
CREATE TABLE IF NOT EXISTS vendor_name_keywords (
    kw text PRIMARY KEY,
    category text
);

CREATE TABLE IF NOT EXISTS purpose_keywords (
    kw text PRIMARY KEY,
    category text
);

/* seed */
INSERT INTO vendor_name_keywords (kw, category) VALUES
  ('media',      'Media & Digital Advertising'),
  ('digital',    'Media & Digital Advertising'),
  ('advert',     'Media & Digital Advertising'),
  ('market',     'Media & Digital Advertising'),
  ('payments',   'Fundraising & Direct-Response'),
  ('consult',    'Consulting & Strategy'),
  ('strateg',    'Consulting & Strategy'),
  ('print',      'Printing & Mail Production'),
  ('mailer',     'Printing & Mail Production'),
  ('sign',       'Printing & Mail Production'),
  ('poll',       'Polling & Research'),
  ('research',   'Polling & Research'),
  ('payroll',    'Payroll & Staff'),
  ('travel',     'Travel & Lodging'),
  ('legal',      'Legal & Compliance')
  ON CONFLICT (kw) DO NOTHING;;

INSERT INTO purpose_keywords (kw, category) VALUES
  ('fundrais',     'Fundraising & Direct-Response'),
  ('direct mail',  'Fundraising & Direct-Response'),
  ('list rental',  'Fundraising & Direct-Response'),
  ('merchant fee', 'Fundraising & Direct-Response'),
  ('processing fee', 'Fundraising & Direct-Response'),
  ('media buy',    'Media & Digital Advertising'),
  ('advert',       'Media & Digital Advertising'),
  ('market',       'Media & Digital Advertising'),  
  ('print',        'Printing & Mail Production'), 
  ('sign',         'Printing & Mail Production'),
  ('poll',         'Polling & Research'),
  ('survey',       'Polling & Research'),
  ('travel',       'Travel & Lodging'),
  ('hotel',        'Travel & Lodging'),
  ('transfer',     'Transfers / Contributions'),
  ('legal',        'Legal & Compliance'),
  ('filing fee',   'Legal & Compliance'),
  ('compliance',   'Legal & Compliance')
  ON CONFLICT (kw) DO NOTHING;;