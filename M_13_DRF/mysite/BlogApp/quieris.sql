
select "BlogApp_article"."id", "BlogApp_article"."title",
"BlogApp_article"."content", "BlogApp_article"."pub_date",
"BlogApp_article"."author_id", "BlogApp_article"."category_id" from "BlogApp_article"; args=(); alias=default


select "BlogApp_author"."id", "BlogApp_author"."name", "BlogApp_author"."bio"
from "BlogApp_author" where "BlogApp_author"."id" = 1 limit 21; args=(1,); alias=default
select "BlogApp_category"."id", "BlogApp_category"."name"
from "BlogApp_category" where "BlogApp_category"."id" = 1 limit 21; args=(1,); alias=default

select "BlogApp_tag"."id", "BlogApp_tag"."name"
from "BlogApp_tag" inner join "BlogApp_article_tags" on ("BlogApp_tag"."id" = "BlogApp_article_tags"."tag_id") where "BlogApp_article_tags"."article_id" = 1; args=(1,); alias=default

----


select "BlogApp_article"."id",
"BlogApp_article"."title",
"BlogApp_article"."content",
"BlogApp_article"."pub_date",
"BlogApp_article"."author_id",
"BlogApp_article"."category_id" from "BlogApp_article"; args=(); alias=default

select "BlogApp_author"."id", "BlogApp_author"."name", "BlogApp_author"."bio" from "BlogApp_author" where "BlogApp_author"."id" = 1 limit 21; args=(1,); alias=default
select "BlogApp_category"."id", "BlogApp_category"."name" from "BlogApp_category" where "BlogApp_category"."id" = 1 limit 21; args=(1,); alias=default
select "BlogApp_tag"."id", "BlogApp_tag"."name" from "BlogApp_tag" inner join "BlogApp_article_tags" on ("BlogApp_tag"."id" = "BlogApp_article_tags"."tag_id") where "BlogApp_article_tags"."article_id" = 1; args=(1,); alias=default
select "BlogApp_author"."id", "BlogApp_author"."name", "BlogApp_author"."bio" from "BlogApp_author" where "BlogApp_author"."id" = 2 limit 21; args=(2,); alias=default
select "BlogApp_category"."id", "BlogApp_category"."name" from "BlogApp_category" where "BlogApp_category"."id" = 2 limit 21; args=(2,); alias=default
select "BlogApp_tag"."id", "BlogApp_tag"."name" from "BlogApp_tag" inner join "BlogApp_article_tags" on ("BlogApp_tag"."id" = "BlogApp_article_tags"."tag_id") where "BlogApp_article_tags"."article_id" = 2; args=(2,); alias=default

---

select "BlogApp_article"."id", "BlogApp_article"."title", "BlogApp_article"."content", "BlogApp_article"."pub_date", "BlogApp_article"."author_id", "BlogApp_article"."category_id", "BlogApp_author"."id", "BlogApp_author"."name", "BlogApp_author"."bio", "BlogApp_category"."id", "BlogApp_category"."name" from "BlogApp_article" inner join "BlogApp_author" on ("BlogApp_article"."author_id" = "BlogApp_author"."id") inner join "BlogApp_category" on ("BlogApp_article"."category_id" = "BlogApp_category"."id"); args=(); alias=default
select ("BlogApp_article_tags"."article_id") as "_prefetch_related_val_article_id", "BlogApp_tag"."id", "BlogApp_tag"."name" from "BlogApp_tag" inner join "BlogApp_article_tags" on ("BlogApp_tag"."id" = "BlogApp_article_tags"."tag_id") where "BlogApp_article_tags"."article_id" in (1, 2); args=(1, 2); alias=default

---

SELECT "BlogApp_article"."id", "BlogApp_article"."title", "BlogApp_article"."pub_date", "BlogApp_article"."author_id", "BlogApp_article"."category_id", "BlogApp_author"."id", "BlogApp_author"."name", "BlogApp_author"."bio", "BlogApp_category"."id", "BlogApp_category"."name" FROM "BlogApp_article" INNER JOIN "BlogApp_author" ON ("BlogApp_article"."author_id" = "BlogApp_author"."id") INNER JOIN "BlogApp_category" ON ("BlogApp_article"."category_id" = "BlogApp_category"."id"); args=(); alias=default
SELECT ("BlogApp_article_tags"."article_id") AS "_prefetch_related_val_article_id", "BlogApp_tag"."id", "BlogApp_tag"."name" FROM "BlogApp_tag" INNER JOIN "BlogApp_article_tags" ON ("BlogApp_tag"."id" = "BlogApp_article_tags"."tag_id") WHERE "BlogApp_article_tags"."article_id" IN (1, 2); args=(1, 2); alias=default

---
SELECT "BlogApp_article"."id", "BlogApp_article"."title", "BlogApp_article"."pub_date", "BlogApp_article"."author_id", "BlogApp_article"."category_id", "BlogApp_author"."id", "BlogApp_author"."name", "BlogApp_category"."id", "BlogApp_category"."name" FROM "BlogApp_article" INNER JOIN "BlogApp_author" ON ("BlogApp_article"."author_id" = "BlogApp_author"."id") INNER JOIN "BlogApp_category" ON ("BlogApp_article"."category_id" = "BlogApp_category"."id"); args=(); alias=default
SELECT ("BlogApp_article_tags"."article_id") AS "_prefetch_related_val_article_id", "BlogApp_tag"."id", "BlogApp_tag"."name" FROM "BlogApp_tag" INNER JOIN "BlogApp_article_tags" ON ("BlogApp_tag"."id" = "BlogApp_article_tags"."tag_id") WHERE "BlogApp_article_tags"."article_id" IN (1, 2); args=(1, 2); alias=default
