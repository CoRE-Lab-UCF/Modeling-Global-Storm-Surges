
function [net_zt, net_zc, net_area, net_width, net_xt, net_xc, Fail, Fail1, Fail2] = ANN_train(delta, Ev_all, Values);%% Prepare output

not = size(delta,1);%size(delta,1); %number of transects

net_zt = cell(not,1);
net_zc = cell(not,1);
net_area = cell(not,1);
net_width = cell(not,1);
net_xt = cell(not,1);
net_xc = cell(not,1);
L(1:not,1:6) = NaN;   %
Call(1:not,1:6) = NaN;%
Ctest(1:not,1:6) = NaN;%


%% Obtain NNs for all transects 

Inp = Values(Ev_all,[2:7]);
Fail(1:not,1:6) = NaN; %

for jj = 1:6

    for ii = 1:not%size(delta,1)
        ii
        for ne = 2:6
            ne
            Out = delta(ii,:,jj)';
            net = feedforwardnet(ne);
            net = configure(net,Inp',Out');

            for zz = 1:50
                zz
                net.trainParam.showWindow = false;
                net.trainParam.showCommandLine = false;

                [net,tr] = train(net,Inp',Out');
                outputs = net(Inp');
                
                f = find(isnan(Out));
                Out(f) = outputs(f);
                
                
                Corr_all(zz,1) = corr(outputs',Out);
                Corr_test(zz,1) = corr(outputs([tr.testInd,tr.valInd])',Out([tr.testInd,tr.valInd]));
                
                if Corr_all(zz,1)>0.8 && Corr_test(zz,1)>0.8
                    Fail1(ii,jj) = 1;
                    break
                end
            end
            
            if Corr_all(zz)>0.8 && Corr_test(zz)>0.8
                Fail2(ii,jj) = 1;
                break
            end
        end
        
        if ne == 2 && zz == 50 % why 2?
            H = Corr_test+Corr_all;
            [~,m] = max(H);
            M1 = Corr_all(m);
            M2 = Corr_test(m);
                            Fail(ii,jj) = 1;

            for yy = 1:200
                net.trainParam.showWindow = false;
                net.trainParam.showCommandLine = false;
                [net,tr] = train(net,Inp',Out');
                outputs = net(Inp');
                f = find(isnan(Out));
                Out(f) = outputs(f);
                Corr_all1(yy,1) = corr(outputs',Out);
                Corr_test1(yy,1) = corr(outputs([tr.testInd,tr.valInd])',Out([tr.testInd,tr.valInd]));
                if Corr_all1(yy,1)>M1*0.9 && Corr_test1(yy,1)>M2*0.9
                    break
                end
                        if zz == 50 && yy == 200
        end
            end 
        end
        
        clear Corr_all Corr_test
        

        
        if jj == 1
            net_zt{ii,1} = net;
        end
        if jj == 2
            net_zc{ii,1} = net;
        end
        if jj == 3
            net_area{ii,1} = net;
        end
        if jj == 4
            net_width{ii,1} = net;
        end
        if jj == 5
            net_xt{ii,1} = net;
        end
        if jj == 6
            net_xc{ii,1} = net;
        end
    end
end


end