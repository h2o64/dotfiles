find DTS/ -follow -type f -exec sed -i 's/qcom,a7_atl/qcom,capricorn_atl/g' {} \;
find DTS/ -follow -type f -exec sed -i 's/qcom,a7_sdi/qcom,capricorn_sdi/g' {} \;
find DTS/ -follow -type f -exec sed -i 's/qcom,b7_atl_3840mah/qcom,natrium_atl_3840mah/g' {} \;
find DTS/ -follow -type f -exec sed -i 's/qcom,a4_coslight/qcom,scorpio_coslight/g' {} \;

