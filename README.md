# Deploy prefect cloud
1. Install uvx
   > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

2. Login to prefect cloud
   > uvx prefect-cloud login

3. Deploy python code from Github
   > uvx prefect-cloud deploy etl_pipeline.py:main_flow --name my_etl --from https://github.com/ekaratnida/Data-Engineer --with-requirements requirements.txt
   
4. Run main_flow function
   > uvx prefect-cloud run main_flow/my_etl

5. Schedule tasks
   > uvx prefect-cloud schedule main_flow/my_etl "*/1 * * * *"

# Google Bigquery
   > https://docs.google.com/presentation/d/1PddRr1WBlpKB4RMzRDgqzrk7q5C97fJU1h9sYWWJDb8/edit?slide=id.g3e4e1b92149_0_396#slide=id.g3e4e1b92149_0_396

# Slide
1. https://drive.google.com/file/d/1PWtTvDy6ingAtutjJLaxuc0d5HuzPAjD/view
2. https://drive.google.com/file/d/1RkNsTUyoP7jqMHA9YXeIX1rINO30EPUT/view
3. https://drive.google.com/file/d/1wQvNgG98w73xqgVRe29OviMzMzfM7Ctd/view
4. https://drive.google.com/file/d/1Hzxh6Zzx3O6Sw4DoUOQRSaoB6nuuBS2j/view 
