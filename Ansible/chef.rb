remote_file "#{Chef::Config[:file_cache_path]}/s3ninja.zip" do
  source node[:s3ninja][:package_source]
end

bash 'extract_app' do
  cwd '/home/s3ninja/'
  code <<-EOH
    unzip #{Chef::Config[:file_cache_path]}/s3ninja.zip
    EOH
  not_if { ::File.exists?('/home/s3ninja/sirius.sh') }
end

execute 'chown -R s3ninja:s3ninja /home/s3ninja/'

file '/home/s3ninja/sirius.sh' do
  mode 00777
end

template '/etc/init.d/s3ninja' do
  source 's3ninja-init.erb'
  mode 0777
  owner 'root'
  group 'root'
end

service 's3ninja' do
  provider Chef::Provider::Service::Init
  action [:start]
end
