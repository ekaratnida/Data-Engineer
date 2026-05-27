# Workshop
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uvx prefect-cloud login

uvx prefect-cloud deploy etl_pipeline.py:main_flow --name my_etl --from https://github.com/ekaratnida/Data-Engineer --with-requirements requirements.txt

uvx prefect-cloud run main_flow/my_etl

uvx prefect-cloud schedule main_flow/my_etl "*/1 * * * *"

# Slide
1. https://drive.google.com/file/d/1PWtTvDy6ingAtutjJLaxuc0d5HuzPAjD/view
2. https://drive.google.com/file/d/1RkNsTUyoP7jqMHA9YXeIX1rINO30EPUT/view
3. https://drive.google.com/file/d/1wQvNgG98w73xqgVRe29OviMzMzfM7Ctd/view
4. https://drive.google.com/file/d/1Hzxh6Zzx3O6Sw4DoUOQRSaoB6nuuBS2j/view 
