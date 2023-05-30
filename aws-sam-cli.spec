Name:           aws-sam-cli
Version:        1.84.0
Release:        1%{?dist}
Summary:        CLI tool to build, test, debug, and deploy Serverless applications using AWS SAM

License:
URL:            https://github.com/aws/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-devel
Requires:

%description
The AWS Serverless Application Model (SAM) CLI is an open-source CLI tool that helps you develop serverless applications containing Lambda functions, Step Functions, API Gateway, EventBridge, SQS, SNS and more.

%package -n python3-aws-sam-cli
Summary: %{summary}

%prep
%autosetup -p1 -n aws-sam-cli-v%{version}

%generate_buildrequires:
%pyproject_buildrequires -t


%build
%pyproject_wheel

%install
%pyproject_install

%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Mon May 15 2023 David Duncan <davdunc@davidduncan.org>
- Initial specfile creation
